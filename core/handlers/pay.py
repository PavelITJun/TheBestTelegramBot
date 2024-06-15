from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardMarkup, InlineKeyboardButton,\
    ShippingOption, ShippingQuery

BY_SHIPPING = ShippingOption(
    id='BY',
    title='Dev_to_BY',
    prices=[
        LabeledPrice(
            label='Dev_by_BelPochta',
            amount=500
        )
    ]
)

RU_SHIPPING = ShippingOption(
    id='RU',
    title='Dev_to_RU',
    prices=[
        LabeledPrice(
            label='Dev_by_PochtaRossii',
            amount=1000
        )
    ]
)

UA_SHIPPING = ShippingOption(
    id='UA',
    title='Dev_to_UA',
    prices=[
        LabeledPrice(
            label='Dev_by_UAPochta',
            amount=1500
        )
    ]
)

CITIES_SHIPPING = ShippingOption(
    id='capitals',
    title='Dev_to_cap',
    prices=[
        LabeledPrice(
            label='Dev_by_Toreto',
            amount=2000
        )
    ]
)


async def shipping_check(shipping_query: ShippingQuery, bot: Bot):
    shipping_options = []
    countries = ['BY', 'RU', 'UA']
    if shipping_query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(shipping_query.id, ok=False, error_message='Can not be devilired')
    if shipping_query.shipping_address.country_code == 'BY':
        shipping_options.append(BY_SHIPPING)
    if shipping_query.shipping_address.country_code == 'RU':
        shipping_options.append(RU_SHIPPING)
    if shipping_query.shipping_address.country_code == 'UA':
        shipping_options.append(UA_SHIPPING)
    cities = ['Минск', 'Москва', 'Киев']
    if shipping_query.shipping_address.city in cities:
        shipping_options.append(CITIES_SHIPPING)
    await bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options)


keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Pay',
            pay=True
        )
    ],
    [
        InlineKeyboardButton(
            text='link',
            url='https://www.google.com'
        )
    ]
])





async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Payment by tg bot',
        description='Learn how to pay by tg',
        payload='Payment with a bot',
        provider_token='381764678:TEST:77550',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Nix',
                amount=10000
            ),
            LabeledPrice(
                label='НДС',
                amount=2000
            ),
            LabeledPrice(
                label='Скидка',
                amount=-2000
            ),
            LabeledPrice(
                label='Bonus',
                amount=-1000
            ),
        ],
        max_tip_amount=100000,
        suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='pavel',
        provider_data=None,
        photo_url='data:image/jpeg;base64,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',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=False,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=True,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=keyboards,
        request_timeout=30
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f'Thanks for payment {message.successful_payment.total_amount // 100} {message.successful_payment.currency}'
    await message.answer(msg)