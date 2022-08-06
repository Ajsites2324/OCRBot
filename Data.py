from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can extract text from images using OCR technology.

By ➪» @PAPA_BOL_SAKTEHO ❤︎

FEELINGS➪» @ABOUT_AJEET
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/AJEET_BOTS")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/AJEET_BOTS")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/ABOUT_AJEET")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/MODERN_ELEMENTS")],
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

Just send an image. Rest is on me.

Note : You can send any amount of images at once and it will work with same speed and accuracy.

More features in development. Keep track by joining @AJEET_BOTS || @ABOUT_AJEET .
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @ABOUT_AJEET

More bots : [Click Here](https://t.me/ajeet_bots)

Source Code : [Click Here](https://t.me/papa_bol_sakteho)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : [𓆩〭⃛〬𓆩〭⃛〬➤⃝✖‿✖•Ajͥeeͣtͫ](https://t.me/papa_bol_sakteho)
    """
