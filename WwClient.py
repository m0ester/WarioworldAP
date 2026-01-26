import asyncio
import time
import traceback
import dolphin_memory_engine as DME
import Utils
import kvui

from typing import TYPE_CHECKING, Optional, Any
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, logger, server_loop
from NetUtils import ClientStatus, NetworkItem
from gamedata import Spriteling, Treasure, BossMedal, StageDoor, Junk, Trap, ITEM_TABLE
from items import WwItem



CONNECTION_REFUSED = (
    "Dolphin failed to connect. Please ensure you are using a Warioworld NTSC ROM. Trying again in 5 seconds..."
)

CONNECTION_LOST = (
    "Connection to Dolphin was lost. Please restart your Emulator and ensure Warioworld is running."
)

CONNECTION_ESTABLISHED = (
    "Dolphin Connected Successfully!"
)

CONNECTION_INITIAL = (
    "Dolphin Connection has not been initiated."
)

currentHP = DME.read_word(DME.follow_pointers(0x801c5820,[0xd8]))

class WwCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx:CommonContext):
        super().__init__(ctx)
    
    def _cmd_dolphin(self) -> None:
        if isinstance(self.ctx, WwContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}") 

class WwContext(CommonContext):
    command_processor = WwCommandProcessor
    game: str = "Warioworld"

    def __init__(self, server_address = Optional[str], password = Optional[str]) -> None:
        super().__init__(server_address, password)
        self.items_received_2: list[tuple[NetworkItem, int]] =[]
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.dolphin_status: str = CONNECTION_INITIAL
        self.awaiting_rom: bool = False
        self.last_rcvd_index: int = -1
        self.has_send_death: bool = False

    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        self.auth = None


    async def server_auth(self, password_requested: bool = False) -> None:
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        if not self.auth:
            if self.awaiting_rom:
                return
            self.awaiting_rom = True
            logger.info("Awaiting connection to Dolphin to get player information.")
            return
        await self.send_connect()

    def on_package(self, cmd, args: dict[str, Any]) -> None:
        if cmd == "Connected":
            self.items_received_2 = []
            self.last_rcvd_index = -1
            if "death_link" in args["slot_data"]:
                Utils.async_start(self.update_death_link(bool(args["slot_data"]["death_link"])))
    
    def on_deathlink(self, data: dict[str, Any]) -> None:
        super().on_deathlink(data)
        _give_death(self)

    def make_gui(self) -> type["kvui.GameManager"]:
            ui = super().make_gui()
            ui.base_title = "Archipelago Warioworld Client"
            return ui
    
def read_short(console_address: int) -> int:
    return int.from_bytes(DME.read_bytes(console_address, 2), byteorder="big")


def write_short(console_address: int, value: int) -> None:
    DME.write_bytes(console_address, value.to_bytes(2, byteorder="big"))

async def check_playable() -> bool:
    if DME.read_word(0x801ce6f4) == 0:
        return False
    return True

async def check_ingame() -> bool:
    if DME.read_word(0x801ce6f4) == 3:
        return False

async def check_alive() -> bool:
    if check_ingame() and  currentHP != 0:
        return True
    return False

async def check_death(ctx: WwContext) -> None:
    if ctx.slot is not None and check_ingame():
        if currentHP <= 0:
            if not ctx.has_send_death and time.time() >= ctx.last_death_link + 3:
                ctx.has_send_death = True
                await ctx.send_death(ctx.player_names[ctx.slot] + " ran out of hearts.")
        else:
            ctx.has_send_death = False

def _give_death(ctx: WwContext) -> None:

    if (
        ctx.slot is not None
        and DME.is_hooked()
        and ctx.dolphin_status == CONNECTION_ESTABLISHED
        and check_alive()
    ):
        ctx.has_send_death = True
        DME.write_word((0x801c5820) + 0xd8, 0)


def _give_item(ctx: WwContext, item_name: str) -> bool:
    if not check_ingame():
        return False
    item_id = ITEM_TABLE[item_name].value
    if WwItem.type == Spriteling.ItemType: #load value in spriteling address, or with spriteling ID, store in spriteling address
        write_short(Spriteling.loc,
                read_short(Spriteling.loc)|Spriteling.value)


async def give_items(ctx: WwContext) -> None:
    """
    Give the player all outstanding items they have yet to receive.
 
    :param ctx: Warioworld client context.
    """
    # Loop through items to give.
    for item, idx in ctx.items_received_2:
        # If the item's index is greater than the player's expected index, give the player the item.
        if ctx.last_item_handled < idx:
            # Attempt to give the item and increment the expected index.
            while not _give_item(ctx):
                await asyncio.sleep(0.01)

            # Increment the expected index.
            ctx.last_item_handled = idx

async def dolphin_sync_task(ctx: WwContext) -> None:
    """
    The task loop for managing the connection to Dolphin.

    While connected, read the emulator's memory to look for any relevant changes made by the player in the game.

    :param ctx: The Wind Waker client context.
    """
    logger.info("Starting Dolphin connector. Use /dolphin for status information.")
    while not ctx.exit_event.is_set():
        try:
            if DME.is_hooked() and ctx.dolphin_status == CONNECTION_ESTABLISHED:
                if not check_ingame():
                    # Reset the give item array while not in the game.
                    #DME.write_bytes(GIVE_ITEM_ARRAY_ADDR, bytes([0xFF] * ctx.len_give_item_array))
                    await asyncio.sleep(0.1)
                    continue
                if ctx.slot is not None:
                    if "DeathLink" in ctx.tags:
                        await check_death(ctx)
                    await give_items(ctx)
                else:
                    if ctx.awaiting_rom:
                        await ctx.server_auth()
                await asyncio.sleep(0.1)
            else:
                if ctx.dolphin_status == CONNECTION_ESTABLISHED:
                    logger.info("Connection to Dolphin lost, reconnecting...")
                    ctx.dolphin_status = CONNECTION_LOST
                logger.info("Attempting to connect to Dolphin...")
                DME.hook()
                if DME.is_hooked():
                    if DME.read_bytes(0x80000000, 6) != b"GWWE01":
                        logger.info(CONNECTION_REFUSED)
                        ctx.dolphin_status = CONNECTION_REFUSED
                        DME.un_hook()
                        await asyncio.sleep(5)
                    else:
                        logger.info(CONNECTION_ESTABLISHED)
                        ctx.dolphin_status = CONNECTION_ESTABLISHED
                        ctx.locations_checked = set()
                else:
                    logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
                    ctx.dolphin_status = CONNECTION_LOST
                    await ctx.disconnect()
                    await asyncio.sleep(5)
                    continue
        except Exception:
            DME.un_hook()
            logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
            logger.error(traceback.format_exc())
            ctx.dolphin_status = CONNECTION_LOST
            await asyncio.sleep(5)
            continue


def main(connect: Optional[str] = None, password: Optional[str] = None) -> None:
    """
    Run the main async loop for Warioworld client.

    :param connect: Address of the Archipelago server.
    :param password: Password for server authentication.
    """
    Utils.init_logging("Mario Kart Double Dash Client")

    async def _main(connect: Optional[str], password: Optional[str]) -> None:
        ctx = WwContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

        # Runs Universal Tracker's internal generator
        #if tracker_loaded:
        #     ctx.run_generator()
        #     ctx.tags.remove("Tracker")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await asyncio.sleep(1)

        ctx.dolphin_sync_task = asyncio.create_task(dolphin_sync_task(ctx), name="DolphinSync")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.dolphin_sync_task:
            await asyncio.sleep(3)
            await ctx.dolphin_sync_task

    import colorama

    colorama.init()
    asyncio.run(_main(connect, password))
    colorama.deinit()