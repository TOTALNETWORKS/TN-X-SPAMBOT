from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("★𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦★", data="help_back")
    ],
    [
        Button.url("★𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥★", "https://t.me/ITACHI_TNs")
    ],
    [
        Button.url("★𝙎𝙐𝙋𝙋𝙊𝙍𝙏★", "https://t.me/TN_BOT_SUPPORT")
    ],
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n"
        await event.client.send_file(
            event.chat_id,
            "https://telegra.ph/file/dc1b6a5fae00e58480a47.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
