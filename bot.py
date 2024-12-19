from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio, random
from config import token

bot = Bot(token=token)
dp = Dispatcher()

choices = [1, 3]

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Привет я Телеграмм бот")

@dp.message(Command("about"))
async def about(message:types.Message):
    about_text = """
        Информация о нас
    """
    await message.answer(about_text)

@dp.message(Command("contact"))
async def contact(message:types.Message):
    await message.answer("""
    Вы можете связаться с нами по следующим контактам:
    - Email: example@example.com
    - Телефон: +7 123 456 7890
"""
)

@dp.message(Command("game"))
async def game(message:types.Message):
    await message.answer("Выберите число от 1 до 3: ")

@dp.message()
async def paly_game(message:types.Message):
    try:
        user_number = int(message.text.strip())
    except ValueError:
        return await message.answer("Пожалуйста введите число от 1 до 3.")

    if user_number < 1 or user_number > 3:
        return await message.answer("Число должно быть от 1 до 3.")

    bot_number = random.randint(1,3)

    if user_number == bot_number:
        result = "Ничья"
    elif user_number > bot_number:
        result = "Вы виграли"
    else:
        result = "ВЫ проиграли"

    await message.answer(f"Ты выбрал {user_number}\nБот выбрал {bot_number}\n{result}")
    await message.answer("Если хотите продолжить нажмите на команду /game")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())