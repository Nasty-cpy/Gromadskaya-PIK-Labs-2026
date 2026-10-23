import math
from .base_function import MathFunction
from .cos_function import CosFunction

class TanFunction(MathFunction):
    """Класс функции Тангенс."""

    def __init__(self, x: float):
        super().__init__(x)

    def calculate(self):
        # ограничение деления на ноль 
        if math.cos(self.x) == 0:
            raise ValueError("Тангенс не определен при cos(x) = 0")
        return math.tan(self.x)

    # Производная тангенса = 1 / cos^2(x).
    def get_derivative(self):
        return CosFunction(self.x)

    def __str__(self):
        return f"Тангенс: tg({self.x}) = {self.calculate():.4f}"