# запись данных в файл
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w') #или
# data = open('file.txt', 'a')
# data.writelines(colors)  # разделителей не будет
# data.write('LINE 121\n')
# data.write('LINE 131\n')
# data.close() #закрытие

# 2способ
# with open('file.txt','a') as data:
#     data.write('LINE 17\n')
#     data.write('LINE 28\n')

# Чтение данных
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
#

# Взять код из другого скрипта
# import lection1_hello
# print(lection1_hello.f(1))


# import lection1_hello as h
# print(h.f(1))

# Функции
#
# def new_string(symbol, count=3):
#     return symbol*count
# print(new_string('!', 5)) #!!!!!
# print(new_string(4)) #12

# неограниченное кол-во параметров
# def concatenatio(*params):
#     res: str = ''
#     for item in params:
#         res += item
#     return res
#
#
# print(concatenatio('a','s', 'd', 'w'))  # asdw
# print(concatenatio('a', '1'))  # a1

# Рекурсия. Числа Фибоначчи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
#
# print(list)

# # Кортеж. Двойное преобразование.
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# вводим кортеж
# x, y =input('введите через пробел').split()
# print(x, y) #это строки
# x, y =[int(i) for i in input('введите через пробел').split()] #списочное выражение, если надо число

#словари
# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# типы ключей могут отличаться

# for k in dictionary.keys(): #все ключи
#     print(k)

# for v in dictionary.values(): # только значения
#      print(v)

# for v in dictionary:
#      print(dictionary[v])
#
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))

#Сколько раз повторяется в словаре
sp=[1, 1, 2, 2, 2, 4] #{1:2, 2:3, 4:1}
slov={}
for el in sp:
    slov[el] = slov.get(el,0) +1
    # if el not in slov:
    #     slov[el] = 1
    # else:
    #     slov[el]+=1
print(slov)
print(slov.get(2)) #поиск значения для ключа 2
print(slov.get(7, 0)) #если нет ключа, то вывести 0




# множества
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# #множество
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}
#
# неизменяемое множество
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

#добавить и удалить элемент из списка
#
# list = [1, 2, 3, 4, 5]
# print(list)
# print(list.pop(2)) #удалить
# print(list)
# print(list.insert(2, 11)) #добавить
# print(list)
# print(list.append(11)) #в конец
# print(list)