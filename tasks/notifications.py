from dotenv import load_dotenv
from create_bot import bot
from img_parser import get_random_img
from datetime import datetime
from logger import log
from util import should_i_send_message_now
import os

load_dotenv()
chat_id = os.environ.get('qa_dream_team_chat_id')


async def change_pass():
    log.info('CRON TRIGGERED change_pass')
    if datetime.now().isocalendar().week % 2 != 0:
        log.info('TODAY IS ODD WEEK, MESSAGE WILL BE SENT')
        await send(query="мемы про пароль", text="Зайдите на VDI и смените пароль")
    else:
        log.info('TODAY IS NOT ODD WEEK, MESSAGE WONT BE SENT')


async def log_jira_time_wednesday():
    log.info('CRON TRIGGERED log_jira_time_wednesday')
    await send(query="мем жаба среда", text="Спишите часы в JIRA")


async def log_jira_time_end_of_month():
    log.info('CRON TRIGGERED log_jira_time_end_of_month')

    if should_i_send_message_now():
        log.info('ALL CHECKS PASSED, MESSAGE WILL BE SENT')
        await send(query="мем последний день", text="Проверьте списание часов в JIRA за весь месяц")
    else:
        log.info('SOME OF CHECKS FAILED, MESSAGE WONT BE SENT')


# async def meeting():
#     log.info('CRON TRIGGERED meeting')
#     #  Если сегодня будний день
#     if datetime.now().weekday() <= 4:
#         log.info('TODAY IS WEEKDAY, MESSAGE WILL BE SENT')
#         await send(query="мем созвон на работе", text="Ежедневный статус через 5 минут")


async def send(query='null', text='null'):
    try:
        img = await get_random_img(query)
        await bot.send_photo(chat_id=chat_id,
                             caption=f"⚠️⚠️⚠️<b>ДЕЖУРНОЕ НАПОМИНАНИЕ</b>⚠️⚠️⚠️\n{text}",
                             photo=img, parse_mode='HTML')
    except Exception:
        await bot.send_message(chat_id=chat_id, text=f"⚠️⚠️⚠️<b>ДЕЖУРНОЕ НАПОМИНАНИЕ</b>⚠️⚠️⚠️\n{text}", parse_mode='HTML')
