# Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import randrange

n = int(input('Введите число: '))
list = []
while len(list) < abs(n):
    list.append(randrange((-1) * abs(n), abs(n)))
print(list)

data = []

with open("file.txt", 'r') as f:
    data = [row.strip() for row in f]

data = [int(i) for i in data]
# print(type(data[0]))
print(f'Индексы: {data}')


result = 1
for i in range(len(data)):
    result *= list[data[i]]

print(f'Произведение элементов на указанных позициях: {result}')
