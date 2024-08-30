import asyncio
from aiogram.utils import executor
from create_bot import dp
from handlers import register_all_handlers

from tasks import scheduler

register_all_handlers(dp)


async def on_startup(_):
    await scheduler()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    loop = asyncio.new_event_loop()
