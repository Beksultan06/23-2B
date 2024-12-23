from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio, logging
from config import token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher()

class UserInfo(StatesGroup):
    name = State()
    phone = State()
    course = State()
    department = State()
    city = State()

student_data = {}

@dp.message(Command("start"))
async def start(message:types.Message, state: FSMContext):
    await message.answer("Добро пожаловать. Давай начнем с твоего имени. Как тебя зовут?")
    await state.set_state(UserInfo.name)

@dp.message(UserInfo.name)
async def name(message:types.Message, state:FSMContext):
    student_data['name'] = message.text
    await message.reply("Введите номер телефона")
    await state.set_state(UserInfo.phone)

@dp.message(UserInfo.phone)
async def phone(message:types.Message, state:FSMContext):
    student_data['phone'] = message.text
    await message.answer("Введите на каком курсе вы учитесь")
    await state.set_state(UserInfo.course)

@dp.message(UserInfo.course)
async def course(message:types.Message, state:FSMContext):
    student_data['course'] = message.text
    await message.answer("Введите в какой кафедре вы учитесь")
    await state.set_state(UserInfo.department)

@dp.message(UserInfo.department)
async def department(message: types.Message, state:FSMContext):
    student_data['department'] = message.text
    await message.answer("Введите город в котором проживаете")
    await state.set_state(UserInfo.city)

@dp.message(UserInfo.city)
async def city(message:types.Message, state:FSMContext):
    student_data['city'] = message.text
    await message.answer(f"Спосибо за информацию! Вот твои данные: \n"
                         f"Имя: {student_data['name']}\n"
                         f"Телефон: {student_data['phone']}\n"
                         f"Курс: {student_data['course']}\n"
                         f"Кафедра: {student_data['department']}\n"
                         f"Город: {student_data['city']}")
    await state.clear()

async def main():
    await dp.start_polling(bot)

asyncio.run(main())