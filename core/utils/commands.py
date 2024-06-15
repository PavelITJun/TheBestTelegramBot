from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='1'
        ),
        BotCommand(
            command="help",
            description='2'

        ),
        BotCommand(
            command='cancel',
            description='3'
        ),
        BotCommand(
            command='inline',
            description='4'
        ),
        BotCommand(
            command='pay',
            description='5'
        ),
        BotCommand(
            command='form',
            description='6'
        ),
        BotCommand(
            command='audio',
            description='audio'
        ),
        BotCommand(
            command='document',
            description='document'
        ),
        BotCommand(
            command='mediagroup',
            description='mediagroup'
        ),
        BotCommand(
            command='photo',
            description='photo'
        ),
        BotCommand(
            command='video',
            description='video'
        ),
        BotCommand(
            command='sticker',
            description='sticker'
        ),
        BotCommand(
            command='video_note',
            description='video_note'
        ),
        BotCommand(
            command='voice',
            description='voice'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())