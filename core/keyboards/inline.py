from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callbackdata import MacInfo


# select_macbook = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text='Macbook Air 13',
#             callback_data='apple_air_13_m1_2020'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='Macbook Pro 14',
#             callback_data='apple_pro_14_m1_2020'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='Pro 16',
#             callback_data='apple_pro_16_i7_2019'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='link',
#             url='https://www.google.com'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='profile',
#             url='tg://user?id=969943952'
#         )
#     ]
# ])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Macbook Air 13', callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
    keyboard_builder.button(text='Macbook Pro 14', callback_data=MacInfo(model='pro', size=14, chip='m1', year=2020))
    keyboard_builder.button(text='Macbook Pro 16', callback_data=MacInfo(model='pro', size=16, chip='i7', year=2019))
    keyboard_builder.button(text='link', url='https://www.google.com')
    keyboard_builder.button(text='profile', url='tg://user?id=969943952')
    keyboard_builder.adjust(3, 1, 1)
    return keyboard_builder.as_markup()