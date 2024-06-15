from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo
from aiogram import Bot
from aiogram.utils.chat_action import ChatActionSender


async def get_audio(message: Message, bot: Bot):
    audio = FSInputFile(path=r'C:\Users\PC\Desktop\zal\booi.mp3', filename="Booi.mp3")
    await bot.send_audio(message.chat.id, audio=audio)


async def get_document(message: Message, bot: Bot):
    document = FSInputFile(path=r'C:\Users\PC\Desktop\zal\word.docx', filename="Word.docx")
    await bot.send_document(message.chat.id, document=document, caption='It is a doc')


async def get_media_group(message: Message, bot: Bot):
    photo1_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\PC\Desktop\zal\g.jpg'),
                                caption='It is a mediagroup')
    photo2_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\PC\Desktop\zal\g.jpg'))
    video_mg = InputMediaVideo(type='video', media=FSInputFile(r'C:\Users\PC\Desktop\zal\videog.mp4'))
    media = [photo1_mg, photo2_mg, video_mg]
    await bot.send_media_group(message.chat.id, media)


async def get_photo(message: Message, bot: Bot):
    photo = FSInputFile(path=r'C:\Users\PC\Desktop\zal\forhtml.jpg')
    await bot.send_photo(message.chat.id, photo, caption='It is just a photo')


async def get_sticker(message: Message, bot: Bot):
    sticker = FSInputFile(r'C:\Users\PC\Desktop\zal\sticker.png')
    await bot.send_sticker(message.chat.id, sticker)


async def get_video(message: Message, bot: Bot):
    video = FSInputFile(r'C:\Users\PC\Desktop\zal\videog.mp4')
    await bot.send_video(message.chat.id, video)


async def get_video_note(message: Message, bot: Bot):
    video_note = FSInputFile(r'C:\Users\PC\Desktop\zal\videognote.mp4')
    await bot.send_video_note(message.chat.id, video_note)


async def get_voice(message: Message, bot: Bot):
    voice = FSInputFile(r'C:\Users\PC\Desktop\zal\booi.opus')
    await bot.send_voice(message.chat.id, voice)