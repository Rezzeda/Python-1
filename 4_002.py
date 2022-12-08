# Найдите корни квадратного уравнения Ax² + Bx + C = 0:

import math

a, b, c = [int(i) for i in input('Введите значения А, В, С: ').split()]
d = b ** 2 - 4 * a * c
x1=0
x2=0
if d > 0:
    x1 = (-b - math.sqrt(d)) / 2 * a
    x2 = (-b + math.sqrt(d)) / 2 * a
    print(f'Корни квадратного уравнения х1={x1}, x2={x2}')
elif d==0:
    x1 = (-b)/ 2 * a
    print(f'Корень квадратного уравнения х1={x1}')
else:
    print('Корней нет')


