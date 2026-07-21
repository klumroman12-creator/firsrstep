from fak import get_fake_user
import json

filename = input("Enter your filename >>>")
amount = int(input("How many users to generate? >>> "))

with open (filename, "w") as file:
    user = []
    for _ in range(amount):
        user.append(json.dumps(get_fake_user(), ensure_ascii=False))

    file.writelines(user)
