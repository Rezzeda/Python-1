# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = []
for i in range(5):
    list.append(int(input('Введите данные: ')))
sum=0
list1=[]
for i in range(len(list)//2+1):
    list1.append(list[i]*list[-1-abs(i)])

print(list1)
