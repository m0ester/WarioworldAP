import asyncio
import time
import traceback
import dolphin_memory_engine as DME
import Utils
import kvui

from NetUtils import ClientStatus
from typing import Optional, Any
from CommonClient import gui_enabled, logger, server_loop
from NetUtils import NetworkItem
from .gamedata import NET_TABLE, CHECK_TABLE, FILLER_TABLE, Bosses_h, Spriteling
from .Items import LOOKUP_ID_TO_NAME
#from .Locations import LOOKUP_NAME_TO_ID, WwLocation
from . import Patches

tracker_loaded = False
try:
    from worlds.tracker.TrackerClient import (TrackerCommandProcessor as ClientCommandProcessor,
                                              TrackerGameContext as CommonContext, UT_VERSION)
    tracker_loaded = True
except ImportError:
    from CommonClient import ClientCommandProcessor, CommonContext

###### Dolphin connection ######
def _apply_ar_code(code: list[int]):
    for i in range(0, len(code), 2):
        command = (code[i] & 0xFE00_0000) >> 24
        address = (code[i] & 0x01FF_FFFF) | 0x8000_0000
        if command == 0x04:
            DME.write_word(address, code[i + 1])

#def _apply_fakegecko(code: dict[int, list[int]]):
 #   for start_address, rows in code.items():
  #      address = start_address
   #     for row in rows:
    #        DME.write_word(address, row)
     #       address += 4

def _apply_gecko(code: list[int]):
    length = 0
    for _ in code:
        length += 8
    start = DME.read_word(0x80000034) - length
    for row in code:
        DME.write_word(start, row>>32)
        DME.write_word(start+4,row&0x00000000FFFFFFFF)
        start += 8
    start = DME.read_word(0x80000034) - length
    for row in code:
        if row & 0xc2ffffff00ffffff and (row&0x00000000ff000000) == 0 and (row&0x00000000ffffffff) != 0:
            c2 = int(row>>32)
            start = start+8
            c2len = int((row&0x0000000000FFFFFF)*8)
            DME.write_word((c2-0x42000000), (start-(c2-0x42000000)+0x48000000))
            DME.write_word(start+c2len-4, abs(start-8+c2len-c2-0x42000000)-0x38000000)
            start = start + c2len

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
PALOFFSET = 0xa840

class WwCommandProcessor(ClientCommandProcessor):
    """
        Command Processor for Warioworld client commands.

        This class handles commands specific to Warioworld."""
    def __init__(self, ctx:CommonContext):
        super().__init__(ctx)
    
    def _cmd_dolphin(self) -> None:
        """Display Dolphin Emulator's current connection status."""
        if isinstance(self.ctx, WwContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}") 

class WwContext(CommonContext):
    command_processor = WwCommandProcessor
    game: str = "Warioworld"
    items_handling: int = 7

    def __init__(self, server_address = Optional[str], password = Optional[str]) -> None:
        super().__init__(server_address, password)
        self.spritelings = 0
        self.slotdata = None
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
    async def update_ring_link(self, ring_link: bool):
        """Helper function to set Ring Link connection tag on/off and update the connection if already connected."""
        old_tags = self.tags.copy()
        if ring_link:
            self.tags.add("RingLink")
        else:
            self.tags -= {"RingLink"}
        if old_tags != self.tags and self.server and not self.server.socket.closed:
            await self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}])


    def on_package(self, cmd, args: dict[str, Any]) -> None:
        super().on_package(cmd, args)
        if cmd == "Connected":
            self.items_received = []
            self.last_rcvd_index = -1
            self.slotdata = args["slot_data"]

            if "death_link" in args["slot_data"]:
                Utils.async_start(self.update_death_link(bool(args["slot_data"]["death_link"])))
            if "ring_link" in args["slot_data"]:
                Utils.async_start(self.update_ring_link(bool(args["slot_data"]["ring_link"])))

            self.spritelingreq = self.slotdata["spriteling requirement"]
            if self.ui:
                self.ui.spritelingcountupdate(self.spritelings, self.spritelingreq)
                #self.ui.doorupdate([])

        if cmd == "Bounce":
            if

    def on_deathlink(self, data: dict[str, Any]) -> None:
        print("ondeathlink")
        super().on_deathlink(data)
        _give_death(self)

    def make_gui(self) -> type["kvui.GameManager"]:
        """Initialises Warioworld GUI
        Returns client GUI"""
        from kvui import GameManager
        base_class: type = GameManager
        ut_title: str = ""
        # Use Universal Tracker gui only if it's recent enough version.
        if tracker_loaded and UT_VERSION >= "v0.2.12":
            base_class = super().make_gui()
            ut_title = f" | Universal Tracker {UT_VERSION}"
        class WwManager(base_class):
            logging_pairs = [("Client", "Archipelago")]
            base_title = f"Archipelago Warioworld Client {ut_title} | Archipelago"

            def build(self):
                container = super().build()
                from kivy.metrics import dp
                from kvui import MDBoxLayout, MDLabel
                from kivymd.uix.fitimage import FitImage

                def get_image(source: str, width: int = 0, height: int = 0) -> FitImage:
                    from importlib import resources
                    from kivy.core.image import Image
                    from io import BytesIO
                    img = resources.files(__package__ + ".icons").joinpath(source)
                    data = img.read_bytes()
                    raw_image = Image(BytesIO(data), ext=img.suffix[1:])
                    image = FitImage(texture=raw_image.texture)
                    if width > 0:
                        image.size_hint_x = None
                        image.width = dp(width)
                    if height > 0:
                        image.size_hint_y = None
                        image.height = dp(height)
                    return image

                layout = MDBoxLayout(
                    orientation="horizontal",
                    size_hint_y=None,
                    height=dp(50),
                    spacing=dp(5),
                    padding=dp(5),
                )
                layout.add_widget(get_image("Spritelings.png", 36, 36))

                self.spritelingcount: MDLabel = MDLabel(text = "0/40", halign = "left", role = "large")
                layout.add_widget(self.spritelingcount)

                self.grid.add_widget(layout)
                return container

            def spritelingcountupdate(self, current: int, goal: int) -> None:
                self.spritelingcount.text =f"{current}/{goal}"

            #def doorupdate(self, doorsopened: list[int]) -> None:
             #   self.spritelingcount.text = f"{doorsopened}"

        return WwManager

def apply_patch():
    logger.info("Applying patch")
    if isPAL():
        _apply_gecko(Patches.PALGeckers)
        _apply_ar_code(Patches.arPALtches)
        logger.info("PALpatch applied")
    else:
        _apply_gecko(Patches.Geckers)
        _apply_ar_code(Patches.arpatches)
        logger.info("NTSCpatch applied")

def currentHP():
    if isPAL():
        return DME.read_word(DME.read_word(0x801d00c0) + 0xd8)
    else:
        return DME.read_word(DME.read_word(0x801c5820)+0xd8)

def HPPtr():
    if isPAL():
        return DME.read_word(0x801d00c0)
    else:
        return DME.read_word(0x801c5820)

def read_short(console_address: int) -> int:
    return int.from_bytes(DME.read_bytes(console_address, 2), byteorder="big")

def write_short(console_address: int, value: int) -> None:
    DME.write_bytes(console_address, value.to_bytes(2, byteorder="big"))

def read_string(console_address: int, strlen: int) -> str:
    return DME.read_bytes(console_address, strlen).split(b"\0", 1)[0].decode()

def isPAL():
    if DME.read_bytes(0x80000000, 6) == b"GWWP01":
        return True
    else:
        return False


def check_ingame() -> bool:
    if isPAL():
        if DME.read_word(0x801ce6f0+PALOFFSET) in [3, 1] and DME.read_word(0x801ce6f4+PALOFFSET) == 0:
            return False
        elif DME.read_double(0x801ce398+PALOFFSET) != 0xFFFFFFFFFFFFFFFF:
            return True
    else:
        if DME.read_word(0x801ce6f0) in {3,1} and DME.read_word(0x801ce6f4) == 0:
            return False
        elif DME.read_double(0x801ce398) != 0xFFFFFFFFFFFFFFFF:
            return True
    return True

def check_pressstart() -> bool:
    if isPAL():
        if DME.read_byte(0x801f9b21) == 1:
            return True
    else:
        if DME.read_byte(0x801ef299) == 1:
            return True
    return False


async def check_alive() -> bool:
    if check_ingame() and  currentHP() != 0:
        return True
    return False

async def check_death(ctx: WwContext) -> None:
    if ctx.slot is not None and check_ingame():
        if currentHP() <= 0:
            if isPAL():
                if DME.read_word(0x801d00c0) == 0:
                    ctx.has_send_death = False
                    return
            else:
                if DME.read_word(0x801c5820) == 0:
                    ctx.has_send_death = False
                    return
            if not ctx.has_send_death and time.time() >= ctx.last_death_link + 3:
                ctx.has_send_death = True
                await ctx.send_death(ctx.player_names[ctx.slot] + " did not have a rotten day.")
        else:
            ctx.has_send_death = False

def check_location(check_name: str) -> bool:
    checked = False
    if isPAL():
        address = CHECK_TABLE[check_name].memloc + PALOFFSET
    else:
        address = CHECK_TABLE[check_name].memloc
    memvalue = CHECK_TABLE[check_name].memvalue
    # If the location is in the current stage, check the bitfields for the current stage as well.
    if not checked:
        if check_name in Bosses_h.keys():
            checked = bool(read_short(address) & memvalue)
        else:
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
        if isPAL():
            address = CHECK_TABLE[location].memloc+PALOFFSET
        else:
            address = CHECK_TABLE[location].memloc
        check_id = CHECK_TABLE[location].CheckID
        memvalue = CHECK_TABLE[location].memvalue
        if check_location(location) or check_id in ctx.checked_locations:
            if location in Bosses_h.keys():
                write_short(address, read_short(address) | memvalue)
            else:
                DME.write_byte(address, DME.read_byte(address) | memvalue)
            if check_location("Victory") and ctx.spritelings >= ctx.slotdata["spriteling requirement"]:
                if not ctx.finished_game:
                    await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                    ctx.finished_game = True
            else:
                await ctx.check_locations([check_id])
    # Send the list of newly-checked locations to the server.
    locations_checked = ctx.locations_checked.difference(ctx.checked_locations)
    if locations_checked:
        await ctx.send_msgs([{"cmd": "LocationChecks", "locations": locations_checked}])

def _give_death(ctx: WwContext) -> None:
    print("died lmao")
    if (
        ctx.slot is not None
        and DME.is_hooked()
        and ctx.dolphin_status == CONNECTION_ESTABLISHED
        and check_alive()
    ):
        ctx.has_send_death = True
        print("sent deathlink")
        if isPAL():
            DME.write_word(DME.read_word(0x801d00c0) + 0xd8, 0)
        else:
            DME.write_word(DME.read_word(0x801c5820) + 0xd8, 0)

def _give_item(ctx: WwContext, item_name: str) -> bool:

    if not check_ingame():
        return False
    else:
        if isPAL():
            address = NET_TABLE[item_name].memloc+PALOFFSET
        else:
            address = NET_TABLE[item_name].memloc
        memvalue = NET_TABLE[item_name].memvalue
    if item_name in FILLER_TABLE.keys():
        if address is None:
            if isPAL():
                address = DME.read_word(0x801d00c0) + 0xd8
            else:
                address = DME.read_word(0x801c5820) + 0xd8
        if FILLER_TABLE[item_name].ItemType == "add":
            DME.write_word(address, (DME.read_word(address) + memvalue))
            return True
        elif FILLER_TABLE[item_name].ItemType == "set":
            DME.write_word(address, memvalue)
            return True
    else:
        write_short(address, read_short(address) | memvalue)
        ctx.ui.spritelingcountupdate(ctx.spritelings, ctx.slotdata["spriteling requirement"])
    return True

async def give_items(ctx: WwContext) -> None:
    """
    Give the player all outstanding items they have yet to receive.
 
    :param ctx: Warioworld client context.
    """
    #check if ingame
    if check_ingame():
        # Check if there are new items.
        if isPAL():
            expected_itemamount = read_short(NETITEMSRECEIVED+PALOFFSET)
        else:
            expected_itemamount = read_short(NETITEMSRECEIVED)
        for idx, item in enumerate(ctx.items_received[expected_itemamount:], start=expected_itemamount):
            if len(ctx.items_received) <= expected_itemamount:
                # There are no new items.
                return
            if expected_itemamount != (len(ctx.items_received)-1) and LOOKUP_ID_TO_NAME[item.item] in FILLER_TABLE.keys():
                #do not give already given filler
                if expected_itemamount < idx+1:
                    if isPAL():
                        write_short(NETITEMSRECEIVED+PALOFFSET, idx+1)
                    else:
                        write_short(NETITEMSRECEIVED, idx+1)
                continue
            # Attempt to give the item and increment the expected index.
            while not _give_item(ctx, LOOKUP_ID_TO_NAME[item.item]):
                await asyncio.sleep(0.01)
            if expected_itemamount < idx+1:
                if isPAL():
                    write_short(NETITEMSRECEIVED + PALOFFSET, idx + 1)
                else:
                    write_short(NETITEMSRECEIVED, idx + 1)
            i=0
            spritelinglist=[]
            while i <= len(ctx.items_received):
                var = LOOKUP_ID_TO_NAME[ctx.items_received[i].item]
                if isinstance(NET_TABLE[var], Spriteling):
                    spritelinglist.append(var)
                i+=1
            ctx.spritelings = len(spritelinglist)
            ctx.ui.spritelingcountupdate(ctx.spritelings, ctx.slotdata["spriteling requirement"])

async def dolphin_sync_task(ctx: WwContext) -> None:
    """
    The task loop for managing the connection to Dolphin.

    While connected, read the emulator's memory to look for any relevant changes made by the player in the game.

    :param ctx: Warioworld client context.
    """
    patched = False
    items_filled = False
    logger.info("Starting Dolphin connector. Use /dolphin for status information.")
    while not ctx.exit_event.is_set():
        try:
            if DME.is_hooked() and ctx.dolphin_status == CONNECTION_ESTABLISHED:
                if check_pressstart() and not check_ingame() and not patched and ctx.auth:
                    apply_patch()
                    patched = True
                    await asyncio.sleep(0.1)
                elif not patched:
                    logger.info("Patching Failed. Please ensure you are on the press start screen and connected to the server")
                    await asyncio.sleep(5)
                    continue
                #item prefill for important cutscene related items
                if not items_filled:
                    if isPAL():
                        loadingfillloopthing = 0x801cf810+PALOFFSET
                    else:
                        loadingfillloopthing = 0x801cf810
                    if DME.read_word(loadingfillloopthing) < 5 :
                        for item in ctx.items_received:
                            itemname = LOOKUP_ID_TO_NAME[item.item]
                            if itemname not in FILLER_TABLE.keys():
                                if isPAL():
                                    write_short(NET_TABLE[itemname].memloc + PALOFFSET, read_short(NET_TABLE[itemname].memloc + PALOFFSET) | NET_TABLE[itemname].memvalue)
                                else:
                                    write_short(NET_TABLE[itemname].memloc, read_short(NET_TABLE[itemname].memloc) | NET_TABLE[itemname].memvalue)
                                if isinstance(NET_TABLE[itemname], Spriteling):
                                    ctx.spritelings +=1
                        ctx.ui.spritelingcountupdate(ctx.spritelings,ctx.slotdata["spriteling requirement"])
                        items_filled=True
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
                    if DME.read_bytes(0x80000000, 6) not in {b"GWWE01", b"GWWP01"}:
                        logger.info(CONNECTION_REFUSED)
                        ctx.dolphin_status = CONNECTION_REFUSED
                        DME.un_hook()
                        patched = False
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
            await ctx.disconnect()
            await asyncio.sleep(5)
            continue

def main(connect: Optional[str] = None, password: Optional[str] = None) -> None:
    """
    Run the main async loop for Warioworld client.

    :param connect: Address of the Archipelago server.
    :param password: Password for server authentication.
    """
    Utils.init_logging("Warioworld Client")

    async def _main(connect: Optional[str], password: Optional[str]) -> None:
        ctx = WwContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

        # Runs Universal Tracker's internal generator
        if tracker_loaded:
             ctx.run_generator()
             ctx.tags.remove("Tracker")

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