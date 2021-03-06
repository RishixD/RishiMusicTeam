# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello π there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\nπ΄ Do you want me to play music in your Telegram groups'voice chats? Please click the \'π User Manual π\' button below to know how you can use me.\n\nπ΄ The Assistant must be in your group to play music in the voice chat of your group.\n\nπ΄ More info & commands mentioned in the [User Manual](http://telegra.ph/NOTES-BY-RISHI-05-18-2).\n\nA project by @RISHI_OP""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π πππ΄π πΌπ°π½ππ°π» π", url="http://telegra.ph/NOTES-BY-RISHI-05-18-2"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β‘ πΎππ½π΄π β‘", url="https://t.me/RISHI_OP"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β‘ π²π·π°π πΆππΎππΏ β‘", url="https://t.me/NiceJokeLol"
                    )
                ],
                [   
                    InlineKeyboardButton(
                        "β‘ π°π±πΎππ πΌπ΄ β‘", url="https://t.me/Definitely_not"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**π΄ πππππ'π πππππ πππ is online π**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β‘ ππ΄πΈππ³πΎ β‘", url="https://t.me/Definitely_not"
                    )
                ]
            ]
        ),
    )
