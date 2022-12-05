# Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие методы из библиотеки random - можно).

from random import sample

list = [1, 2, 3, 4, 5]
list1 = []
list1.append(sample(list, len(list)))
print(*list1)
