from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Haii.. ๐๐ป {message.from_user.first_name} Welcome to ๐Virtual Music๐\n
๐๐๐ ๐๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐ ๐๐๐ ๐๐ ๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐ : [KING](https://t.me/boyfriendnice)

๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐๐ ๐๐ ๐ ๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐ ๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐๐, ๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐ ๐.
โโโโโโโโโโโโโโโ
โฃ > ๐น๐ฐ๐ฝ๐ถ๐ฐ๐ฝ ๐ป๐ธ๐๐ ๐ป๐ฐ๐ถ๐ ๐๐ด๐บ๐ฐ๐ป๐ธ๐ถ๐๐ ๐๐ฐ๐บ๐๐ ๐ด๐๐พ๐.
โฃ > ๐น๐ธ๐บ๐ฐ ๐ท๐ฐ๐ฑ๐ธ๐ ๐ณ๐ธ๐ผ๐ฐ๐๐ธ๐บ๐ฐ๐ฝ ๐ฟ๐ฐ๐บ๐๐ฐ ๐น๐ฐ๐ฝ๐ถ๐ฐ๐ฝ
โฃ > ๐ป๐ฐ๐ฝ๐ถ๐๐๐ฝ๐ถ ๐ฟ๐ป๐ฐ๐ ๐ป๐ฐ๐ถ๐ ๐๐๐ฝ๐ถ๐ถ๐ ๐๐ด๐ฑ๐ด๐ฝ๐๐ฐ๐
โฃ > ๐น๐ธ๐บ๐ฐ ๐๐ธ๐ณ๐ฐ๐บ, ๐ฐ๐๐ธ๐๐๐ด๐ฝ ๐๐ธ๐ณ๐ฐ๐บ ๐ฐ๐บ๐ฐ๐ฝ ๐ฝ๐ฐ๐ธ๐บ.
โโโโโโโโโโโโโโโ
๐คต๐๐ป๐ฎ๐ช๐ฝ๐ฎ๐ญ ๐ซ๐ : [KING](https://t.me/boyfriendnice)
โ๏ธ๐ฃ๐ฑ๐ช๐ท๐ด๐ผ ๐ฏ๐ธ๐ป : [Grup Support](https://t.me/kawan_virtuals)
โโโโโโโโโโโโโโ
๐๐๐ ๐๐๐๐๐ : @virtualsongbot - ๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐ : @AsisstantMusicVirtual

</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "๐ฆOwner", url="https://t.me/imssysbd")
                  ],[
                    InlineKeyboardButton(
                        "๐ฅOfficial Group", url="https://t.me/Familythunder"
                    ),
                    InlineKeyboardButton(
                        "๐ขOfficial Channel", url="https://t.me/MusikManagement") 
                  ],[
                    InlineKeyboardButton(
                        "๐Instagram", url="https://www.instagram.com/ikyyy_35/"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aku sudah online, ayo kita joget ceria! ๐ถ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฆOwner", url="https://t.me/boyfriendnice"
                    )
                ],[
                    InlineKeyboardButton(
                        "โ Yes!", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "โ No!", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**Klik tombol dibawah untuk melihat panduan menggunakan bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฆ Cara Memakai Bot Music!", url="https://t.me/humangabutguys/91577"
                    )
                ]
            ]
        ),
    )
