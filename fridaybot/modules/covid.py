from datetime import datetime

from covid import Covid

covid = Covid(source="worldometers")
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd


@borg.on(admin_cmd(pattern="^!corona$"))
async def iqless(e):
    await e.edit(
        "Antivirus scan was completed \n⚠️ Warning! This  donkey has Corona Virus"
    )


@borg.on(admin_cmd(pattern="^!covid (.*)"))
async def corona(event):
    await event.edit("`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid()
    country_data = covid.get_status_by_country_name(country)
    covid.get_total_deaths()
    if country_data:
        output_text = f"`Confirmed`   :   {country_data['confirmed']}\n"
        output_text += f"`Active`          :   {country_data['active']}\n"
        output_text += f"`Deaths`          :   {country_data['deaths']}\n"
        output_text += f"`Recovered`   :   {country_data['recovered']}\n\n"
        output_text += f"---------TOTAL----------\n\n"
        output_text += f"`Deaths`          :   {covid.get_total_deaths()}\n"
        output_text += f"`Recovered`   :   {covid.get_total_recovered()}\n"
        output_text += f"`Confirmed`   :   {covid.get_total_confirmed_cases()}\n"
        output_text += f"`Active`          :   {covid.get_total_active_cases()}\n\n"
        output_text += (
            "`Update`        :  "
            f"{datetime.utcfromtimestamp(country_data['last_update'] // 1000).strftime('%H:%M')}[GMT]\n"
        )
    else:
        output_text = "Invalid Country name"
    await event.edit(f"Corona Virus Info in {country}:\n\n{output_text}")


@borg.on(admin_cmd(pattern="^!covid2 (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@NovelCoronaBot"
    await event.edit("`Processing covid Info...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1124136160)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```please unlock @NovelCoronaBot```")
            return
        if response.text.startswith("Country"):
            await event.edit("`Invalid Country name`")
        else:
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "covid": "!corona\
\nUsage: slap the taged user\
\n\n!covid <country>\
\nUsage: Get an information about data covid-19 in your country..\
\n\n!covid2 <country>\
\nUsage: same like !covid  \
\n\nSudo Commands ( type !help sudo for more info)\
\n.covid  , .covid2 , .corona \
"
    }
)
