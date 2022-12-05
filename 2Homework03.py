#	Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.
n = int(input('Введите число: '))
result = 0
for i in range(1, n + 1):
    result = round((1+1/i)**i, 2)
    print(result, end=' ')
