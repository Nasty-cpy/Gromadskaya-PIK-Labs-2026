import math
from .base_function import MathFunction


class CosFunction(MathFunction):
    """Класс функции Косинус."""

    def __init__(self, x: float):
        super().__init__(x)

    # Переопределение метода родителя
    def calculate(self):
        return math.cos(self.x)

    # Производная косинуса = минус синус. 
    def get_derivative(self):
        from .sin_function import SinFunction
        return SinFunction(self.x)

    def __str__(self):
        return f"Косинус: cos({self.x}) = {self.calculate():.4f}"