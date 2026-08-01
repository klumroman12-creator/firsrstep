with open('cats.txt', 'w', encoding='utf-8') as f:
    f.write("""60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
""")

def get_cats_info(path):
    try:
        cats = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                parts = line.split(',')
                id = parts[0]
                name = parts[1]
                age = parts [2]
                cats.append({'id': id, 'name': name,'age': age})
        return cats
    except FileNotFoundError:
        print ('Файл не знайдено, спробуйте ще раз!')
        return []

cats_info = get_cats_info("cats.txt")
print(cats_info)

for cat in cats_info:
    print(cat)



