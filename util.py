from datetime import datetime
import calendar
from logger import log


def should_i_send_message_now():
    today = datetime.now()

    # Сперва узнаем количество дней в текущем месяце
    _, last_day = calendar.monthrange(today.year, today.month)

    # Если сегодня последний день месяца и будний день - то True
    if (today.day == last_day) and (today.weekday() <= 4):
        log.info('TODAY IS WEEKDAY AND THE LAST DAY OF MONTH')
        return True


    # Eсли сегодня пятница - то нужно проверить не выпадает ли последний день на сб-вск, если да - True
    if (today.weekday() == 4)\
            and (today.day + 7 > last_day)\
            and (datetime(today.year, today.month, last_day).weekday() >= 5):
        log.info('TODAY IS FRIDAY AND THE LAST DAY OF MONTH IS SATURDAY OR SUNDAY')
        return True


print(should_i_send_message_now())
