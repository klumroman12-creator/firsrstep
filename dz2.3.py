import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def check_directory(directory_path, indent=""):
    if not directory_path.exists():
        print("Такого шляху не існує")
        return
    for item in directory_path.iterdir():
        if item.name.startswith(".") or item.name == "__pycache__":
            continue
        if item.is_dir():
            print(f'{indent}{Fore.BLUE}{item.name}')
            check_directory(item, indent + "    ")
        else:
            print(f'{indent}{Fore.GREEN}{item.name}')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        dir_path = Path(sys.argv[1])
        check_directory(dir_path)
    else:
        print(f'{Fore.RED}Помилка: будь ласка введіть шлях до директорії')
        
                  


