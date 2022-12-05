import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import InputFile

ID = <ID>
API_TOKEN = <TOKEN>

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def send_to_telgram(text: str):
    async def send_message():
        try:
            await bot.send_message(ID, text=text)

        except Exception as e:
            print(e)

    asyncio.run(send_message())
