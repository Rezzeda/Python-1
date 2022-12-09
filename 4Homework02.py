# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))
list = []
for i in range(2, n):
    while n > 2:
        if (n % i) == 0:
            n = n // i
            list.append(i)
        else:
            i += 1
print(list)
