# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randrange

li = [randrange(1, 11) for i in range(5)]
li2 = [(li[i], li[-1 - abs(i)]) for i in range(len(li) // 2 + 1)]
li1 = [li[i] * li[-1 - abs(i)] for i in range(len(li) // 2 + 1)]

li3 = list(zip(li1, li2))

print(li)
print(li2)
print(li1)
print(li3)
