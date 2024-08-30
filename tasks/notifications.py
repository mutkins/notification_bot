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
        img = await get_random_img("мемы про пароль")
        await bot.send_photo(chat_id=chat_id,
                             caption="⚠️⚠️⚠️<b>ДЕЖУРНОЕ НАПОМИНАНИЕ</b>⚠️⚠️⚠️\nЗайдите на VDI и смените пароль",
                             photo=img, parse_mode='HTML')
    else:
        log.info('TODAY IS NOT ODD WEEK, MESSAGE WONT BE SENT')


async def log_jira_time_wednesday():
    log.info('CRON TRIGGERED log_jira_time_wednesday')
    img = await get_random_img("мем жаба среда")
    await bot.send_photo(chat_id=chat_id,
                         caption="⚠️⚠️⚠️<b>ДЕЖУРНОЕ НАПОМИНАНИЕ</b>⚠️⚠️⚠️\nСпишите часы в JIRA",
                         photo=img, parse_mode='HTML')


async def log_jira_time_end_of_month():
    log.info('CRON TRIGGERED log_jira_time_end_of_month')

    if should_i_send_message_now():
        log.info('ALL CHECKS PASSED, MESSAGE WILL BE SENT')
        img = await get_random_img("мем последний день")
        await bot.send_photo(chat_id=chat_id,
                             caption="⚠️⚠️⚠️<b>ДЕЖУРНОЕ НАПОМИНАНИЕ</b>⚠️⚠️⚠️\nПроверьте списание часов в JIRA за весь месяц",
                             photo=img, parse_mode='HTML')
    else:
        log.info('SOME OF CHECKS FAILED, MESSAGE WONT BE SENT')


async def meeting():
    #  Если сегодня будний день
    if datetime.now().weekday() <= 4:
        log.info('CRON TRIGGERED meeting')
        img = await get_random_img("мем созвон на работе")
        await bot.send_photo(chat_id=chat_id,
                             caption="⚠️⚠️⚠️<b>ДЕЖУРНОЕ НАПОМИНАНИЕ</b>⚠️⚠️⚠️\nЕжедневный статус через 5 минут",
                             photo=img, parse_mode='HTML')
