import os
import requests
from StarkChat import starkchat
from pyrogram import *
from pyrogram.types import *

chatbot = starkchat.StarkChat()

API_ID = "25359006" 
API_HASH = "be0a35f4b38dc45f094e64e783d5492b"
BOT_TOKEN = "5711225344:AAFxce6HiKev0RUf2y4yUjq_ge0kyd9WdUk"
CHAT_ID = "-1001663726645"
KEY = "17671b6c-7157-4d20-aaa8-00cc888c8786"

bot = Client("STARK", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@bot.on_message(filters.text)
async def response(client, message):
        question = message.text
        user_id = message.from_user.id
        try:
            r = requests.get(f"http://starkgpt.starkai.live/api?client_id={user_id}&message={question}&key="{KEY}"")
            reply = r.json()["message"]
            await message.reply(reply)
            TEXT = f"**Question:** `{question}`\n**Response:** `{reply}`\n**Engine:** `API`"
            await bot.send_message(chat_id=CHAT_ID,text=TEXT)
            return
        except Exception:
             reply = chatbot.chat(question)
             await message.reply(reply)
             TEXT = f"**Question:** `{question}`\n**Response:** `{reply}`\n**Engine:** `Library`"
             await bot.send_message(chat_id=CHAT_ID,text=TEXT)
             return


def main():
     bot.run()


if __name__ == "__main__":
     main()
