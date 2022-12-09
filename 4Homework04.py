# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Задайте степень: '))
uravnen = ''
while k > 1:
    uravnen = uravnen + f' {randint(0, 100)}x**{k} +'
    k -= 1
# print(f'{uravnen} {randint(0, 100)} = 0')

with open('mnogochlen1.txt', 'w') as data:
# with open('mnogochlen2.txt', 'w') as data:
    data.write(f'{uravnen} {randint(0, 100)} = 0')
