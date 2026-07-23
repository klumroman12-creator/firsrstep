import random 

def get_numbers_ticket(min, max, quantity):
     if min >= 1 and max <= 1000 and quantity >= 1 and quantity <= max:
          numbers = set()
          while len(numbers) < quantity:
            numbers.add(random.randint(min, max))
          return sorted(numbers)
     else:
        return[]    

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
