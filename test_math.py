import unittest
from lab_python_oop.sin_function import SinFunction
from lab_python_oop.cos_function import CosFunction

class TestMathFunctions(unittest.TestCase):
    """Класс для тестирования наших математических функций."""

    def test_sin_zero(self):
        """Проверяем, что синус от 0 равен 0."""
        a = SinFunction(0)
        self.assertAlmostEqual(a.calculate(), 0)

    def test_cos_zero(self):
        """Проверяем, что косинус от 0 равен 1."""
        a = CosFunction(0)
        self.assertAlmostEqual(a.calculate(), 1)

    def test_sin_derivative(self):
        """Проверяем, что производная синуса создает объект косинуса."""
        a = SinFunction(1.5)
        derivative = a.get_derivative()
        # Проверяем, что тип производной - это CosFunction
        self.assertIsInstance(derivative, CosFunction)

# Этот блок запускает тесты, если файл запущен напрямую
if __name__ == '__main__':
    unittest.main()