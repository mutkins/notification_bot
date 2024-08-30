import os
from logger import log
from aiogram import Bot, Dispatcher, types


def check_admin_rights(func):
    async def wrapper(message: types.Message):
        log.info(f'!!!ADMIN ACTION ATTEMPT: {func}, user = {message.from_user.username}')
        if str(message.from_user.id) == str(os.environ.get('my_chat_id')):
            log.info(f'PERMISSION GRANTED')
            await func(message)
        else:
            log.warning(f'PERMISSION DENIED')
    return wrapper
