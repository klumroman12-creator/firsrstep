import datetime

def get_days_from_today(date):
    try:
        today_date = datetime.datetime.today().date()  # перетворюємо в об'єкт datatime
        input_date = datetime.datetime.strptime (date, "%Y-%m-%d").date()
    except ValueError: 
        return "Неправильний формат дати. Спробуйте РРРР-ММ-ДД"

    difference = today_date - input_date # обчислюємо різницю у днях
    return difference.days

print(get_days_from_today("2025-11-12"))

