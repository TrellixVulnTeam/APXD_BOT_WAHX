import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.chru$")
@borg.on(admin_cmd(pattern=r"chru"))
async def bluedevilchru(chru):
    await chru.edit(M)

M = ("┌────┐░░░┌┐░░░░░\n"
"│┌┐┌┐│░░░││░░░░░\n"
"└┘││└┼──┐│└─┐░░░\n"
"░░││░│┌┐││┌┐│░░░\n"
"░░││░│└┘│││││░░░\n"
"░░└┘░└──┘└┘└┘░░░\n"
"┌┐┌─┐░░░░░░░░░░░\n"
"│││┌┘░░░░░░░░░░░\n"
"│└┘┘░┌──┬┬──┬──┐\n"
"│┌┐│░│┌┐├┤──┤│─┤\n"
"│││└┐│┌┐│├──││─┤\n"
"└┘└─┘└┘└┴┴──┴──┘\n"
"┌┐░░░░░░░░░░░░░░\n"
"││░░░░░░░░░░░░░░\n"
"│└─┬──┬┐░░░░░░░░\n"
"│┌┐│┌┐├┤░░░░░░░░\n"
"││││┌┐││░░░░░░░░\n"
"└┘└┴┘└┴┘░░░░░░░░\n"
"┌──┬──┬──┐░░░░░░\n"
"│┌┐│┌┐│┌┐│░░░░░░\n"
"│┌┐│┌┐│└┘│░░░░░░\n"
"└┘└┴┘└┤┌─┘░░░░░░\n"
"░░░░░░││░░░░░░░░\n"
"░░░░░░└┘░░░░░░░░\n"
"┌┐░░░░░░░░░░░░░░\n"
"││░░░░░░░░░░░░░░\n"
"││┌──┬──┐░░░░░░░\n"
"│││┌┐│┌┐│░░░░░░░\n"
"│└┤└┘│└┘│░░░░░░░\n"
"└─┴──┴─┐│░░░░░░░\n"
"░░░░░┌─┘│░░░░░░░\n"
"░░░░░└──┘░░░░░░░\n")
P = ("╔══╗░░░░╔╦╗░░╔═════╗\n"
"║╚═╬════╬╣╠═╗║░▀░▀░║\n"
"╠═╗║╔╗╔╗║║║╩╣║╚═══╝║\n"
"╚══╩╝╚╝╚╩╩╩═╝╚═════╝\n")
K = ("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
"█░░║║║╠─║─║─║║║║║╠─░░█\n"
"█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
G = ("▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
"▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒\n"
"▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒\n"
"▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄\n"
"▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▀█▄\n"
"▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▀\n"
"▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒\n"
"▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒\n"
"▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒\n"
"▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒\n"
"▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒\n"
"▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒\n"
"▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒\n"
"▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
"▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
"▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
"██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
"██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
"█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
"█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
"████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
"████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n")
D = ("───────█████████████████████\n"
"────████▀─────────────────▀████\n"
"──███▀───────────────────────▀███\n"
"─██▀───────────────────────────▀██\n"
"█▀───────────────────────────────▀█\n"
"█─────────────────────────────────█\n"
"█─────────────────────────────────█\n"
"█─────────────────────────────────█\n"
"█───█████─────────────────█████───█\n"
"█──██▓▓▓███─────────────███▓▓▓██──█\n"
"█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█\n"
"█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█\n"
"█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█\n"
"▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀\n"
"──█▄────▀█████▀─────▀█████▀────▄█\n"
"─▄██───────────▄█─█▄───────────██▄\n"
"─███───────────██─██───────────███\n"
"─███───────────────────────────███\n"
"──▀██──██▀██──█──█──█──██▀██──██▀\n"
"───▀████▀─██──█──█──█──██─▀████▀\n"
"────▀██▀──██──█──█──█──██──▀██▀\n"
"──────────██──█──█──█──██\n"
"──────────██──█──█──█──██\n"
"──────────██──█──█──█──██\n"
"──────────██──█──█──█──██\n"
"──────────██──█──█──█──██\n"
"───────────█▄▄█▄▄█▄▄█▄▄█\n"
)
H = ("╭━━━╮╭━━━╮╭━━━╮╭━━━╮\n"
"┃╭━╮┃┃╭━╮┃┃╭━╮┃╰╮╭╮┃\n"
"┃┃╱╰╯┃┃╱┃┃┃┃╱┃┃╱┃┃┃┃\n"
"┃┃╭━╮┃┃╱┃┃┃┃╱┃┃╱┃┃┃┃\n"
"┃╰┻━┃┃╰━╯┃┃╰━╯┃╭╯╰╯┃\n"
"╰━━━╯╰━━━╯╰━━━╯╰━━━╯\n")
E = ("░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄☆\n"
"░███████████████████████\n"
"░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤\n"
"╬▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n"
"▒░░▓▓▓▓▓▓█▄▄▄▄▄█▀╬░\n"
"░░█▓▓▓▓▓▌░▒▒▒▒▒▒▒▒▒\n"
"░▐█▓▓▓▓▓░░▒▒▒▒▒▒▒▒▒\n"
"░▐██████▌╬░▒▒▒▒▒▒▒▒\n"
)
@borg.on(admin_cmd(pattern=r"smil"))
async def bluedevilsmil(smil):
    await smil.edit(P)
@borg.on(admin_cmd(pattern=r"wlcmm"))
async def bluedevilwlcmm(wlcmm):
    await wlcmm.edit(K)
@borg.on(admin_cmd(pattern=r"devl"))
async def bluedevildevl(devl):
    await devl.edit(G)
@borg.on(admin_cmd(pattern=r"dhead"))
async def bluedevildhead(dhead):
    await dhead.edit(D)
@borg.on(admin_cmd(pattern=r"gdd"))
async def bluedevilgdd(gdd):
    await gdd.edit(H)
@borg.on(admin_cmd(pattern=r"pis"))
async def bluedevilpis(pis):
    await pis.edit(E)
