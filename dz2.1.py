with open('salaries.txt', 'w', encoding='utf-8') as f:
    f.write("""Alex Korp,35000
Nikita Borisenko,15000
Sitarama Raju,40000""")


def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            total = 0 
            count = 0 
            for line in f: 
                line = line.strip()
                parts = line.split(',')
                salary = int(parts[1])
                total += salary
                count += 1
            average = total / count
            return total, average 
    except FileNotFoundError:
        print('Файл не знайдено, спробуйте ще раз')
        return 0, 0

total, average = total_salary('salaries.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    

