import sqlite3
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from app.states import Student, student_data
from app.utils import schedule_task
from aiogram.filters import Command
from app.db import saveto_db

student_router = Router()

@student_router.message(Student.name)
async def name(message:types.Message, state:FSMContext):
    student_data['name'] = message.text
    await message.reply("Введите ваш номер телефона")
    await state.set_state(Student.phone)

@student_router.message(Student.phone)
async def phone(message:types.Message, state:FSMContext):
    student_data['phone'] = message.text
    await message.reply("Введите ваш возраст")
    await state.set_state(Student.age)

@student_router.message(Student.age)
async def age(message:types.Message, state:FSMContext):
    student_data['age'] = message.text
    await message.reply("Введите свой класс")
    await state.set_state(Student.lesson)

@student_router.message(Student.lesson)
async def  lesson(message:types.Message, state:FSMContext):
    student_data['lesson'] = message.text
    await message.reply("Напишите свое задание")
    await state.set_state(Student.task)

@student_router.message(Student.task)
async def  task(message:types.Message, state:FSMContext):
    student_data['task'] = message.text
    await message.reply("Когда нужно выаолнить задание (в формате дд.мм.гг чч.мм)")
    await state.set_state(Student.deadline)

@student_router.message(Student.deadline)
async def deadline(message: types.Message, state: FSMContext):
    from datetime import datetime
    try:
        print(f"Получено сообщение: {message.text}")
        deadline_time = datetime.strptime(message.text.strip(), "%d.%m.%Y %H:%M")
        student_data['deadline'] = deadline_time
        saveto_db(student_data)
        await message.answer(f"Задание будет выполнено в {deadline_time.strftime('%d.%m.%Y %H:%M')}")
        await schedule_task(deadline_time)
        await state.clear()
    except ValueError as e:
        print(f"Ошибка преобразования даты: {e}")
        await message.reply("Неверный формат даты, пожалуйста, используйте формат 'дд.мм.гг чч.мм'.")

@student_router.message(Command("tasks"))
async def tasks(message: types.Message):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("select name, task, deadline FROM students where chat_id = ?", (message.chat.id,))
    rows = cursor.fetchall()

    if rows:
        tasks = "\n".join([f"{name} : {task} (до {deadline})" for name, task, deadline in rows])
        await message.answer(f"Ваши задания:\n{tasks}")
    else:
        await message.answer("У вас нет заданий")

    conn.close()