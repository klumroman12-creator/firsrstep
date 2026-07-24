import re

raw_numbers = [
"    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   ",
]

def normalize_phone(phone_number):
    sanitized_phone = re.sub (r'[^\d+]', '', phone_number)

    if sanitized_phone.startswith('+'):
        return sanitized_phone
    elif sanitized_phone.startswith("38"):
        return "+" + sanitized_phone
    else:
        return "+38" + sanitized_phone

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:"  )
for num in sanitized_numbers:
    print(num)
