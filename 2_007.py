# По данному целому числу N распечатайте все квадраты натуральных чисел,
# не превосходящие N, в порядке возрастания.

n = int(input('введите число N'))
for i in range(1, int(n**0.5)):
    if ((i**2)<n):
        print(i**2)