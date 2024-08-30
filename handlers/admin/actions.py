from aiogram import types
from handlers.other.check_permissions import check_admin_rights


@check_admin_rights
async def get_log(message: types.Message):
    file = types.InputFile('main.log')
    await message.answer_document(file)
