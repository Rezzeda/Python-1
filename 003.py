#Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

print('введите n')
number =int(input()) 

for i in range (-number, number+1):
    print(i, end=' ')