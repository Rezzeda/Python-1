# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 2, 2, 3, 4]  -> [1, 3, 4]

li = list(input('Введите данные через пробел: ').split(' '))
res = list(filter(lambda x: li.count(x) == 1, li))
print(res)
