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
        f"""Hello 👋 there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n🔴 Do you want me to play music in your Telegram groups'voice chats? Please click the \'📜 User Manual 📜\' button below to know how you can use me.\n\n🔴 The Assistant must be in your group to play music in the voice chat of your group.\n\n🔴 More info & commands mentioned in the [User Manual](http://telegra.ph/NOTES-BY-RISHI-05-18)\n\nA project by @RISHI_OP""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 𝚄𝚂𝙴𝚁 𝙼𝙰𝙽𝚄𝙰𝙻 📜", url="http://telegra.ph/NOTES-BY-RISHI-05-18"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡ 𝙾𝚆𝙽𝙴𝚁 ⚡", url="https://t.me/RISHI_OP"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡ 𝙲𝙷𝙰𝚃 𝙶𝚁𝙾𝚄𝙿 ⚡", url="https://t.me/NiceJokeLol"
                    )
                ],
                [   
                    InlineKeyboardButton(
                        "⚡ 𝙰𝙱𝙾𝚄𝚃 𝙼𝙴 ⚡", url=" https://t.me/Definitely_not"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**🔴 𝐑𝐈𝐒𝐇𝐈'𝐒 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 is online 😈**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ 𝚆𝙴𝙸𝚁𝙳𝙾 ⚡", url="https://t.me/Definitely_not"
                    )
                ]
            ]
        ),
    )
