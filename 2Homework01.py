# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# o	6782 -> 23
# o	0.56 -> 11

n = input('Введите число: ')
sum = 0
for i in range(len(n)):
    if n[i].isdigit():
        sum += int(n[i])
print(sum)
