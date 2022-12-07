# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = []
for i in range(5):
    list.append(int(input('Введите данные: ')))
sum=0
for i in range(1, len(list)):
    if i % 2 != 0:
        sum += list[i]
print(sum)
