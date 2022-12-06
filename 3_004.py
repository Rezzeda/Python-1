# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
number = 12
list = []
for i in range(5):
    list.append(input('Введите данные: '))

# for i in range(len(list)):
#     if str(number) in list[i]:
#         n=1
#
# if n:
#     print(f'Да')
# else:
#     print('Нет')
if any(str(number)for el in list):
    print(f'Да')