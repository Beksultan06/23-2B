from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from app.states import Student, student_data

start_router = Router()

@start_router.message(Command("start"))
async def start(message:types.Message, state:FSMContext):
    student_data['chat_id'] = message.chat.id
    await message.answer("Привет я бот для учета ваших занятий. Напишите ваше имя!")
    await state.set_state(Student.name)