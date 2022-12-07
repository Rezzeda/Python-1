# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n):
    if n in [-1, 2]:
        return 1
    if (n < -1):
        return ((-1)**(n+1))*fib(abs(n))
    else:
        return fib(n - 1) + fib(n - 2)
list = []
for e in range(-10, 5):
    list.append(int(fib(e)))

print(list)
