from aiogram import Dispatcher
from handlers.admin.actions import get_log


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(get_log, state='*', commands=['log'])

