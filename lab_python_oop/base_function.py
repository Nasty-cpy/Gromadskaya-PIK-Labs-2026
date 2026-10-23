import math

class MathFunction:
    """
    Базовый класс для математической функции от одной переменной
    """
    def __init__(self, x: float): #конструктор  селф ссылка на объект класса, х передача переменно типа флоат
        # Приватная переменная (инкапсуляция)
        self.__x = x

    # Свойство (property) для получения значения переменной
    @property
    #функция возвращает значение х
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        # Ограничение на данные 
        if not isinstance(value, (int, float)):
            raise ValueError("Переменная должна быть числом")
        self.__x = value

    def calculate(self):
        # Базовый метод вычисления. Наследники(син кос тг) его переопределят.
        return self.x

    def get_derivative(self):
        # Метод получения производной.
        return self

    # Строковое представление
    def __str__(self):
        return f"Функция от x={self.x}"