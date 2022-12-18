# Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет,
# можно ли из этих отрезков составить треугольник.

a = 7
b = 6
c = 10


def triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    return False


print(triangle(a, b, c))
