import asyncpg
from aiogram import Bot, Dispatcher
import asyncio
import logging
from core.handlers.basic import *
from aiogram.types import Message
from core.settings import *
from aiogram import F
from aiogram.filters import Command
from core.handlers.contact import *
from core.filters.iscontact import *
from core.utils.commands import *
from core.handlers.callback import *
from core.utils.callbackdata import *
from core.handlers.pay import *
from core.middlewares.officehours import *
from core.middlewares.dbmiddleware import *
from core.handlers import form, send_media
from core.utils.statesform import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers import apshed
from datetime import datetime, timedelta
from core.middlewares.apschedulermiddleware import *
from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler_di import ContextSchedulerDecorator
from core.handlers.send_media import *
from aiogram.utils.chat_action import ChatActionMiddleware
from core.middlewares.example_chat_action_middleware import *


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s.%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    pool_connect = await asyncpg.create_pool(user='postgres', password='198273', database='users2',
                                       host='127.0.0.1', port=5432, command_timeout=60)
    storage = RedisStorage.from_url('redis://localhost:6379/0')
    dp = Dispatcher(storage=storage)
    jobstores = {
        'default': RedisJobStore(jobs_key='dispatched_trips_jobs',
                                 run_times_key='ispatched_trips_running',
                                 db=4,
                                 port=6379)
    }
    scheduler = ContextSchedulerDecorator(AsyncIOScheduler(timezone='Europe/Moscow', jobstores=jobstores))
    scheduler.ctx.add_instance(bot, declared_class=Bot) #изза этой фигни в нижних функциях мы удалим кварги
    # scheduler.add_job(apshed.send_message_time, trigger='date', run_date=(datetime.now() + timedelta(seconds=10)),
    #                   kwargs={'bot': bot})
    # scheduler.add_job(apshed.send_message_cron, trigger='cron', hour=datetime.now().hour,
    #                   minute=datetime.now().minute + 1, start_date=datetime.now(), kwargs={'bot': bot})
    # scheduler.add_job(apshed.send_message_interval, trigger='interval', seconds=60, kwargs={'bot': bot})
    scheduler.start()
    # dp.update.middleware.register(SchedulerMiddleware(scheduler))

    dp.message.middleware.register(ChatActionMiddleware())

    dp.message.register(send_media.get_audio, Command(commands='audio'), flags={'chat_action': 'upload_document'})
    dp.message.register(send_media.get_document, Command(commands='document'), flags={'chat_action': 'upload_document'})
    dp.message.register(send_media.get_media_group, Command(commands='mediagroup'), flags={'chat_action': 'upload_photo'})
    dp.message.register(send_media.get_photo, Command(commands='photo'), flags={'chat_action': 'upload_photo'})
    dp.message.register(send_media.get_sticker, Command(commands='sticker'), flags={'chat_action': 'choose_sticker'})
    dp.message.register(send_media.get_video, Command(commands='video'), flags={'chat_action': 'upload_video'})
    dp.message.register(send_media.get_video_note, Command(commands='video_note'), flags={'chat_action': 'upload_video_note'})
    dp.message.register(send_media.get_voice, Command(commands='voice'), flags={'chat_action': 'upload_voice'})

    dp.message.register(form.get_form, Command(commands='form'))
    dp.message.register(form.get_name, StepsForm.GET_NAME)
    dp.message.register(form.get_last_name, StepsForm.GET_LAST_NAME)
    dp.message.register(form.get_age, StepsForm.GET_AGE)
    dp.update.middleware.register(DbSession(pool_connect))
    dp.update.middleware.register(OfficeHoursMiddleware())
    dp.shipping_query.register(shipping_check)
    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.SUCCESSFUL_PAYMENT)
    #dp.callback_query.register(select_macbook, F.data.startswith('apple_'))
    dp.callback_query.register(select_macbook, MacInfo.filter())
    dp.message.register(get_inline, Command(commands='inline'))
    dp.message.register(get_location, F.location)
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, F.text.lower() == 'привет')
    dp.startup.register(start_bot)
    dp.shutdown.register(finish_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())