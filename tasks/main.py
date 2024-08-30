from tasks.notifications import log_jira_time_wednesday, log_jira_time_end_of_month, change_pass, meeting
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from logger import log


async def scheduler():
    # Инициализация планировщика
    scheduler = AsyncIOScheduler()

    # Каждый будний день. Фильтр внутри
    scheduler.add_job(meeting, CronTrigger(hour=10, minute=55))
    # Каждую среду
    scheduler.add_job(log_jira_time_wednesday, CronTrigger(day_of_week=2, hour=17, minute=30))
    # В последний день месяца. Крон на каждый день, а внутри фильтрация, ибо всё сложно
    scheduler.add_job(log_jira_time_end_of_month, CronTrigger(hour=16, minute=30))
    # Каждую вторую пятницу. Триггер срабатывает каждую пятницу, а внутри уже фильтр
    scheduler.add_job(change_pass, CronTrigger(day_of_week=4, hour=16, minute=00))

    # Запуск планировщика
    scheduler.start()
    log.info('SCHEDULER ACTIVATED')

