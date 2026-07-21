name = (input("Введіть ваше імʼя:  "))

try:
    hours = int(input("Скільки годин ви граєте?: "))
except ValueError:
    hours = 0
except ZeroDivisionError:
    print("It's problem for me")
    
message = f"Welcome to the game {name} you have been playing {hours}"
print(message)