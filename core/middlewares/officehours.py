from datetime import datetime
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from aiogram.types import Message, TelegramObject


def office_hours() -> bool:
    return datetime.now().weekday() in ([f for f in (range(1, 6))]) and datetime.now().hour in ([i for i in range(0, 10)])


class OfficeHoursMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not office_hours():
            return await handler(event, data)

        await event.answer('Time is not for working with this bot')