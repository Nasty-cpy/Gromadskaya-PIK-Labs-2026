import sys

def getnumber(name, index):  #2 параметра
    # Если коэффициент есть в командной строке, то используем его
    if len(sys.argv) > index: #скрипт длч командной строки, сравниваем длину списка аргументов с номером index 
        try:
            return float(sys.argv[index])
        except ValueError:
            print("Неверное значение " + name)

    # Повторяем ввод с клавитуры
    while True:
        try:
            return float(input(name + " = "))
        except ValueError:
            print("нужно действительное число")


def reshenie(a, b, c):
    # Замена y = x^2.
    # Получаем a*y^2 + b*y + c = 0

    d = b ** 2 - 4 * a * c
    print("D =", d) #дискримант 

    if d < 0:
        print("Действительных корней нет")
        return

    y1 = (-b + d ** 0.5) / (2 * a)
    y2 = (-b - d ** 0.5) / (2 * a)

    if y1 >= 0:
        x = y1 ** 0.5
        print("x1,2 =", -x, x)

    if y2 >= 0 and y2 != y1:
        x = y2 ** 0.5
        print("x3,4 =", -x, x)


def main():
    print("a*x^4 + b*x^2 + c = 0")

    a = getnumber("A", 1)

    # A не может быть = 0 
    while a == 0:
        print("A не может быть равен 0")
        a = getnumber("A", 1)

    b = getnumber("B", 2)
    c = getnumber("C", 3)

    print("\nA = " + str(a))
    print("B = " + str(b))
    print("C = " + str(c))

    reshenie(a, b, c)


main()

