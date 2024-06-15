from aiogram import Bot
from aiogram.types import Message
from core.settings import settings
import json
from core.utils.commands import *
from core.keyboards.reply import *
from core.keyboards.inline import *
from core.utils.dbconnect import *


async def get_inline(message: Message, bot: Bot):
    await message.answer(f'This function shows inline kb', reply_markup=get_inline_keyboard())


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Bot is started')


async def finish_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot is finished')


async def get_start(message: Message, bot: Bot, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await bot.send_message(message.chat.id, 'Дарова', reply_markup=get_reply_keyboard())
    json_str = json.dumps(message.model_dump(), default=str)
    print(json_str)


async def get_location(message: Message, bot: Bot):
    await message.answer(f'You have sent your location\r\a'
                         f'{message.location.latitude}\r\n{message.location.longitude}')


async def get_photo(message: Message, bot: Bot):
    await message.answer('You have send a photo, it is downloaded')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')