from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='1 row, 1 button'
        ),
        KeyboardButton(
            text='1 row, 2 button'
        ),
        KeyboardButton(
            text='1 row, 3 button'
        )
    ],
    [
        KeyboardButton(
            text='2 row, 1 button'
        ),
        KeyboardButton(
            text='2 row, 2 button'
        ),
        KeyboardButton(
            text='2 row, 3 button'
        ),
        KeyboardButton(
            text='2 row, 4 button'
        ),
    ],
    [
        KeyboardButton(
            text='3 row, 1 button'
        ),
        KeyboardButton(
            text='3 row, 2 button'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Choose a button', selective=True)

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Share location',
            request_location=True
        ),
        KeyboardButton(
            text='Share my contact',
            request_contact=True
        ),
        KeyboardButton(
            text='Make a poll', #type can be a quiz/regular
            request_poll=KeyboardButtonPollType()
        )
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Share loc/contact or make a poll', selective=True)


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Button 1')
    keyboard_builder.button(text='Button 2')
    keyboard_builder.button(text='Button 3')
    keyboard_builder.button(text='Share loc', request_location=True)
    keyboard_builder.button(text='Share contact', request_contact=True)
    keyboard_builder.button(text='Make a poll', request_poll=KeyboardButtonPollType())
    keyboard_builder.adjust(3, 2, 1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=False,
                                      input_field_placeholder='Share loc/contact or make a poll')