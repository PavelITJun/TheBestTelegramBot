from aiogram.types import Message
from aiogram import Bot
from core.filters.iscontact import *

async def get_true_contact(message: Message, bot: Bot, phone: str):
    await message.answer(f'Ты отправил <b>свой</b> контакт, {phone}')


async def get_fake_contact(message: Message, bot: Bot):
    await message.answer('Ты отправил <b>не свой</b> контакт')