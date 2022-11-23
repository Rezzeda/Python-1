#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
num = 0
maxnum = 0
while num<5:
    number =int(input('введите число')) 
    if number > maxnum:
        maxnum = number
        num+=1
print(maxnum)

# sp = list()
# for i in range(5):
#     n = int(input())
#     sp.append(n)
# print(max(sp))
