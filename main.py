from colorama import Fore, Style, init
from lab_python_oop.sin_function import SinFunction
from lab_python_oop.cos_function import CosFunction
from lab_python_oop.tan_function import TanFunction

# Инициализируем colorama (сторонняя библиотека)
init(autoreset=True)

def main():
    # Выбор типа объекта пользователем
    print("\nВыберите функцию для демонстрации:")
    print("1. Синус")
    print("2. Косинус")
    print("3. Тангенс")
    
    choice = input("Ваш выбор (1-3): ")
    

    # Создаем объект в зависимости от выбора
    if choice == '1':
        try:
            x_val = float(input("Введите значение аргумента x (например, 1.57): "))
        except ValueError:
            print(Fore.RED + "Ошибка: введите число!")
            return
        a = SinFunction(x_val)
        
    elif choice == '2':
        try:
            x_val = float(input("Введите значение аргумента x (например, 1.57): "))
        except ValueError:
            print(Fore.RED + "Ошибка: введите число!")
            return
        a = CosFunction(x_val)
        
    elif choice == '3':
        try:
            x_val = float(input("Введите значение аргумента x (например, 1.57): "))
        except ValueError:
            print(Fore.RED + "Ошибка: введите число!")
            return
        a = TanFunction(x_val)
        
    else:
        print(Fore.RED + "Неверный выбор!")
        return
    print(Fore.GREEN + "\nРезультат работы ")
    

    print(Fore.GREEN + "\nРезультат работы ")
    
    
        # Вызов print для экземпляра класса (сработает __str__)
    print(a)
        
        # Демонстрация метода базового класса
    print(f"Значение функции: {a.calculate():.4f}")
        
        # Демонстрация производной
    derivative = a.get_derivative()
    print(f"Производная в этой точке (базовый класс): {derivative}")
        
    
if __name__ == "__main__":
    main()