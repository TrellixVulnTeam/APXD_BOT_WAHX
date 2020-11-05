from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd


@borg.on(admin_cmd("ascii ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```reply to media message```")
        return
    chat = "@asciiart_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Wait making ASCII...```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=164766745)
            )
            await borg.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @asciiart_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await borg.send_file(event.chat_id, response.message.media)


CMD_HELP.update(
    {
        "ascii": "`.ascii` reply to any image file:\
      \nUSAGE:makes an image ascii style, try out your own.\
      "
    }
)
