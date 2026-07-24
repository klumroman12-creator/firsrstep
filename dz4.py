from datetime import datetime, timedelta

users = [
    {"name": "Oleh", "birthday": "2010.07.30"},
    {"name": "Andriy", "birthday": "1994.11.22"},
    {"name": "Sasha", "birthday": "2005.01.25"}
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо рядок у дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Беремо день народження в цьому році
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо ДН у цьому році вже минув, беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
        # Рахуємо різницю в днях
        days_until = (birthday_this_year - today).days
        
        # Перевіряємо, чи ДН протягом наступних 7 днів (включаючи сьогодні)
        if 0 <= days_until <= 6:
            congratulation_date = birthday_this_year
            
            # Якщо припадає на суботу (5) або неділю (6) — переносимо на понеділок
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)
                
            # Додаємо у фінальний список
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Перевірка роботи функції:
print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))

    

    




