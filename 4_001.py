# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
my_list = [int(i) for i in input('введите через пробел: ').split()]
print(f'Максимум = {max(my_list)}; минимум = {min(my_list)}')