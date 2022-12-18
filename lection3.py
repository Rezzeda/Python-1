# # def sum(x, y):
# #     return x + y
#
# # f=sum
# # f=lambda q,w: q+w
# # sum = lambda x, y: x + y  # то же самое
#
# def mult(x, y):
#     return x * y
#
# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)
#
# # calc(mult, 4, 5)
# # calc(f, 4, 5)
# # calc(sum, 4, 5)
# calc(lambda x, y: x + y, 4, 5)

# LIST COMPREHENSIONS
# list =[]
#
# for i in range(1, 21):
#     if (i%2==0):
#         list.append(i)
# print(list)
#

# a, b, c = [int(i) for i in input("Введите значения A,B,C: ").split()]
# list=[i for i in range(1,21) if (i%2==0)] #то же самое
#  созаем пару каждого из чисел => добавим кортежи
# list=[(i, i) for i in range(1,21) if (i%2==0)]
#  Добавим функцию:

# def f(x):
#     return x**3
# list=[(i, f(i)) for i in range(1,21) if (i%2==0)]
# print(list)

# Задача:  в файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа)
# path = 'ссылка'
# f = open(path, 'r')
# data = f.read() + ' '  # счиываем все, что есть в строчке и искуственно добавляем пробел
# f.close()
# numbers = []
#
# while data != '':  # пробегаемся по всей строке и проверяем, пока строка не пустая
#     space_pos = data.index(' ')  # находим первую позицию пробела и берем все, что находится до него, превращаем в число и добавляем в список
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
#
# out = []
# for e in numbers:
#     if not e % 2: #проверяем на четность
#         out.append((e, e ** 2)) #добавляем кортеж
#
# print(out)

#ЧТО МОЖНО УЛУЧШИТЬ?

# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split() #для примера берем не из файла
# res = select(int, data) #дает список чисел
# res = where(lambda x: not x%2, res) #даст список только четных чисел
# res = select(lambda x:(x, x**2), res)
# print(res)

# ФУНКЦИЯ map
# li = [x for x in range(1, 20)]
#
# li = map(lambda x:x+10, li) #получим map object
# li = list(map(lambda x:x+10, li)) # явное преобразование
# print(li)

# data = map(int,input().split())#по умолч. пробел, если надо , то split(',')
#print(data)
# data = list(map(int,'1 2 3 4 555 6'.split())) #резельтат map итератор, его можно использовать 1 раз
# #чтобы работать этими данными, нужно их "принудительно" сохранить, для этого list
# #проверка
# for e in data:
#     print(e)
# print('---')
# for e in data:
#     print(e)

#посмотрим на предыдущую задачу:
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data) #дает список чисел
# res = where(lambda x: not x%2, res) #даст список только четных чисел
# res = list(map(lambda x:(x, x**2), res))
# print(res)

#Функция filter()
# data = [x for x in range(10)]
#
# # res = filter(lambda x:x%2==0, data) #filter object
# res = list(filter(lambda x: not x % 2, data))
# print(res)

#посмотрим на предыдущую задачу:
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data) #дает список чисел
# res = filter(lambda x: not x%2, res) #даст список только четных чисел
# res = list(map(lambda x:(x, x**2), res))
# print(res)

#Функция zip()

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333] # zip "отрежет" по мин. кол-ву
#
# data = list(zip(users, ids, salary))
# print(data)

#Функция enumerate()
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
#
# data = list(enumerate(users))
# print(data)

sp=['rrrr', 'df', 'zdsf', 'hjtdgf']
# sp.sort(key=lambda a: -len(a))
sp.sort(key=lambda a: len(a), reverse=True )
print(sp)