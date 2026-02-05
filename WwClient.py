import asyncio
import time
import traceback
import dolphin_memory_engine as DME
import Utils
import kvui

from NetUtils import ClientStatus
from typing import Optional, Any
from CommonClient import ClientCommandProcessor, CommonContext, gui_enabled, logger, server_loop
from NetUtils import NetworkItem
from .gamedata import ITEM_TABLE, FILLER_TABLE, CHECK_TABLE, Doors_h, CHECK, LOOKUP_checkID_TO_NAME
from .Items import LOOKUP_ID_TO_NAME, WwItem
#from .Locations import LOOKUP_NAME_TO_ID, WwLocation
from . import Patches

###### Dolphin connection ######
def _apply_ar_code(code: list[int]):
    for i in range(0, len(code), 2):
        command = (code[i] & 0xFE00_0000) >> 24
        address = (code[i] & 0x01FF_FFFF) | 0x8000_0000
        if command == 0x04:
            DME.write_word(address, code[i + 1])

def _apply_fakegecko(code: dict[int, list[int]]):
    for start_address, rows in code.items():
        address = start_address
        for row in rows:
            DME.write_word(address, row)
            address += 4

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
SLOTNAMEADDR = 0x80003f88
SAVEFILEADDR = 0x801ce3a4
SAVEFILELEN = 0xC8
CODEFILEADDR = 0X80002330
NETITEMSRECEIVED = 0X801ce3d4
class WwCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx:CommonContext):
        super().__init__(ctx)
    
    def _cmd_dolphin(self) -> None:
        if isinstance(self.ctx, WwContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}") 

class WwContext(CommonContext):
    command_processor = WwCommandProcessor
    game: str = "Warioworld"
    items_handling: int = 7

    def __init__(self, server_address = Optional[str], password = Optional[str]) -> None:
        super().__init__(server_address, password)
        self.items_receivedd: list[NetworkItem] =[]
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.dolphin_status: str = CONNECTION_INITIAL
        self.awaiting_rom: bool = False
        self.last_rcvd_index: int = -1
        self.has_send_death: bool = False

    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        self.auth = None

    async def server_auth(self, password_requested: bool = False) -> None:
        """
        Authenticate with the Archipelago server.

        :param password_requested: Whether the server requires a password. Defaults to `False`.
        """
        if password_requested and not self.password:
            await super(WwContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

#    async def server_auth(self, password_requested: bool = False) -> None:
 #       if password_requested and not self.password:
  #          await super().server_auth(password_requested)
   #     if not self.auth:
    #        if self.awaiting_rom:
     #           return
      #      self.awaiting_rom = True
       #     logger.info("Awaiting connection to Dolphin to get player information.")
        #    return
        #await self.send_connect()

    def on_package(self, cmd, args: dict[str, Any]) -> None:
        super().on_package(cmd, args)
        if cmd == "Connected":
            self.items_received = []
            self.last_rcvd_index = -1
            #if len(self.items_receivedd) == 0:
                #self.stored_data["savedata"] = (DME.read_bytes(SAVEFILEADDR, SAVEFILELEN))
            if "death_link" in args["slot_data"]:
                Utils.async_start(self.update_death_link(bool(args["slot_data"]["death_link"])))
                print("connectpackage")

        elif cmd == "ReceivedItems":
            for item in args["items"]:
                newitem = ITEM_TABLE[LOOKUP_ID_TO_NAME[item.item]]
                self.items_receivedd.append(item)
                write_short(newitem.memloc, newitem.memvalue | read_short(newitem.memloc))
                print("gotitem")

    def on_death_link(self, data: dict[str, Any]) -> None:
        super().on_deathlink(data)
        _give_death(self)

    def make_gui(self) -> type["kvui.GameManager"]:
            ui = super().make_gui()
            ui.base_title = "Archipelago Warioworld Client"
            return ui

def apply_patch(ctx: WwContext):
    _apply_fakegecko(Patches.patch)
    _apply_ar_code(Patches.arpatches)

def currentHP():
    return DME.read_word(DME.read_word(0x801c5820)+0xd8)

def HPPtr():
    return DME.read_word(0x801c5820)

def read_short(console_address: int) -> int:
    return int.from_bytes(DME.read_bytes(console_address, 2), byteorder="big")

def write_short(console_address: int, value: int) -> None:
    DME.write_bytes(console_address, value.to_bytes(2, byteorder="big"))

def read_string(console_address: int, strlen: int) -> str:
    return DME.read_bytes(console_address, strlen).split(b"\0", 1)[0].decode()

def check_playable() -> bool:
    if DME.read_word(0x801ce6f4) == 0:
        return False
    else:
        return True

def check_ingame() -> bool:
    if DME.read_word(0x801ce6f0) == 3:
        return False
    else:
        return True

def check_pressstart() -> bool:
    if DME.read_byte(0x801ef299) == 1:
        return True
    else:
        return False


async def check_alive() -> bool:
    if check_ingame() and  currentHP() != 0:
        return True
    return False

async def check_death(ctx: WwContext) -> None:
    if ctx.slot is not None and check_ingame():
        if currentHP() <= 0:
            if not ctx.has_send_death and time.time() >= ctx.last_death_link + 3:
                ctx.has_send_death = True
                await ctx.send_death(ctx.player_names[ctx.slot] + " ran out of hearts.")
        else:
            ctx.has_send_death = False

def check_location(check_name: str) -> bool:
    checked = False
    memvalue = CHECK_TABLE[check_name].memvalue
    address = CHECK_TABLE[check_name].memloc
    # If the location is in the current stage, check the bitfields for the current stage as well.
    if not checked:
        checked = bool(DME.read_byte(address) & memvalue)
    return checked

async def check_locations(ctx: WwContext) -> None:
    """
    Iterate through all locations and check whether the player has checked each location.

    Update the server with all newly checked locations since the last update. If the player has completed the goal,
    notify the server.

    :param ctx: The Warioworld client context.
    """
    # Loop through all locations to see if each has been checked.
    for location in CHECK_TABLE.keys():
        check_id = CHECK_TABLE[location].CheckID
        if check_location(location):
            if check_id is None:
                if not ctx.finished_game:
                    await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                    ctx.finished_game = True
            else:
                address = CHECK_TABLE[location].memloc
                memvalue = CHECK_TABLE[location].memvalue
                ctx.locations_checked.add(check_id)
                DME.write_byte(address, DME.read_byte(address) | memvalue)
                print(hex(address), check_id)
    # Send the list of newly-checked locations to the server.
    locations_checked = ctx.locations_checked.difference(ctx.checked_locations)
    if locations_checked:
        await ctx.send_msgs([{"cmd": "LocationChecks", "locations": locations_checked}])

def _give_death(ctx: WwContext) -> None:

    if (
        ctx.slot is not None
        and DME.is_hooked()
        and ctx.dolphin_status == CONNECTION_ESTABLISHED
        and check_alive()
    ):
        ctx.has_send_death = True
        print("sent deathlink")
        DME.write_word(DME.read_word(0x801c5820) + 0xd8, 0)
    else:
        ctx.has_send_death = False

def _give_item(ctx: WwContext, item_name: str) -> bool:

    if not check_ingame():
        return False
    else:
        memvalue = ITEM_TABLE[item_name].memvalue
        address = ITEM_TABLE[item_name].memloc
        write_short(address, read_short(address) | memvalue)
        #ctx.stored_data["savedata"] = (DME.read_bytes(SAVEFILEADDR, SAVEFILELEN))
        print("saved to server, given items")
        return True

async def give_items(ctx: WwContext) -> None:
    """
    Give the player all outstanding items they have yet to receive.
 
    :param ctx: Warioworld client context.
    """
    #check if ingame
    if check_ingame():
        # Check if there are new items.
        expected_itemamount = read_short(NETITEMSRECEIVED)
        if len(ctx.items_receivedd) <= expected_itemamount:
            # There are no new items.
            return
        for idx, item in enumerate(ctx.items_receivedd[expected_itemamount:]):
            # Attempt to give the item and increment the expected index.
            while not _give_item(ctx, LOOKUP_ID_TO_NAME[item.item]):
                await asyncio.sleep(0.01)
            write_short(NETITEMSRECEIVED, expected_itemamount + 1)

async def dolphin_sync_task(ctx: WwContext) -> None:
    """
    The task loop for managing the connection to Dolphin.

    While connected, read the emulator's memory to look for any relevant changes made by the player in the game.

    :param ctx: Warioworld client context.
    """
    patched = False
    loaded = False
    logger.info("Starting Dolphin connector. Use /dolphin for status information.")
    while not ctx.exit_event.is_set():
        try:
            if DME.is_hooked() and ctx.dolphin_status == CONNECTION_ESTABLISHED:
                if check_pressstart() and not check_ingame() and not patched:
                    apply_patch(ctx)
                    logger.info("Patch Applied! loading savefile...")
                    patched = True
                    await asyncio.sleep(0.1)
                elif not patched:
                    logger.info("Patching Failed. Please ensure you are on the press start screen")
                    await asyncio.sleep(5)
                    continue
                if ctx.auth is not None and not loaded:
                    #DME.write_bytes(SAVEFILEADDR, ctx.stored_data["savedata"])
                    logger.info("Savefile Loaded!")
                    loaded = True
                elif not loaded:
                    logger.info("Savefile not loaded, please connect to the server.")
                    await asyncio.sleep(5)
                    continue
                if not check_ingame():
                    await asyncio.sleep(0.1)
                    continue
                if ctx.slot is not None:
                    if "DeathLink" in ctx.tags:
                        await check_death(ctx)
                    await give_items(ctx)
                    await check_locations(ctx)
                else:
                    #if not ctx.auth:
                     #   ctx.auth = read_string(SLOTNAMEADDR, 0x40)
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
                    print("hooked")
                    if DME.read_bytes(0x80000000, 6) != b"GWWE01":
                        logger.info(CONNECTION_REFUSED)
                        ctx.dolphin_status = CONNECTION_REFUSED
                        DME.un_hook()
                        print("gamburger")
                        patched = False
                        await asyncio.sleep(5)
                    else:
                        print("connected")
                        logger.info(CONNECTION_ESTABLISHED)
                        ctx.dolphin_status = CONNECTION_ESTABLISHED
                        ctx.locations_checked = set()
                else:
                    logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
                    ctx.dolphin_status = CONNECTION_LOST
                    await ctx.disconnect()
                    await asyncio.sleep(5)
                    continue
        except RuntimeError:
            continue
        except Exception:
            DME.un_hook()
            logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
            patched = False

            logger.error(traceback.format_exc())
            ctx.dolphin_status = CONNECTION_LOST
            await ctx.disconnect()
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

    import colorama as colourama

    colourama.init()
    asyncio.run(_main(connect, password))
    colourama.deinit()