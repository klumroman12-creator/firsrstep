with open('users.txt', mode='r+') as file:
    file.write("Roman\n")
    file.write("Annn\n")
    file.seek(0)
    print (file.tell())
    print(file.read(5))
    print (file.tell())
    print(file.read(2))


