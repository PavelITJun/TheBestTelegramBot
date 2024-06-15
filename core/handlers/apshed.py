from aiogram import Bot


# async def send_message_time(bot: Bot):
#     await bot.send_message(969943952, 'sent in a few seconds after start')
#
#
# async def send_message_cron(bot: Bot):
#     await bot.send_message(969943952, 'Every day')
#
#
# async def send_message_interval(bot: Bot):
#     await bot.send_message(969943952, 'That is clear')


async def send_message_middleware(bot: Bot, chat_id: int):
    await bot.send_message(chat_id, 'This message made with middleware')
