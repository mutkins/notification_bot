import os
from create_bot import bot


async def send_error_report(error_msg):
    await bot.send_message(text=error_msg, chat_id=os.environ.get('my_chat_id'), parse_mode='HTML')