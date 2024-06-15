from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers.apshed import *
from datetime import datetime, timedelta
from aiogram import Bot
from apscheduler_di import ContextSchedulerDecorator

async def get_form(message: Message, state: FSMContext):
    await message.answer('Как вас зовут?')
    await state.set_state(StepsForm.GET_NAME)


async def get_name(message: Message, state: FSMContext):
    await message.answer('Теперь фамилию')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)


async def get_last_name(message: Message, state: FSMContext):
    await message.answer('Возраст теперь')
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_AGE)


async def get_age(message: Message, bot: Bot, state: FSMContext): #, apscheduler: ContextSchedulerDecorator
    context_data = await state.get_data()
    await message.answer(f'Your data: {str(context_data)}')
    await state.clear()
    # apscheduler.add_job(send_message_middleware, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
    #                     kwargs={"chat_id": message.from_user.id})