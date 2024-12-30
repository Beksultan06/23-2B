from aiogram import Bot, Dispatcher, types
import asyncio, logging, os
from dotenv import load_dotenv
from aiogram.filters import Command
from app.command import router as command
from app.register import router as register
from app.button import keybourd_main

logging.basicConfig(level=logging.DEBUG)

load_dotenv ()

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Привет пожалуйста продите регистрацию!", reply_markup=keybourd_main)

async def main():
    dp.include_routers(command)
    dp.include_routers(register)

    await dp.start_polling(bot)

asyncio.run(main())