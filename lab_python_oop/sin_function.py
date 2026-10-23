import math
from .base_function import MathFunction

# клас синус наследует от класса матери матфунк
class SinFunction(MathFunction):
    """Класс функции Синус"""
    
    def __init__(self, x: float): #селф ссылка на объкт х типа флоат
        super().__init__(x) # обращение к род классу выполнить конструктор и передать значение х

    # Переопределение метода родителя
    def calculate(self):
        return math.sin(self.x)

    # Производная синуса = косинус
    def get_derivative(self):
        from .cos_function import CosFunction
        return CosFunction(self.x)

    def __str__(self):
        return f"Синус: sin({self.x}) = {self.calculate():.4f}"