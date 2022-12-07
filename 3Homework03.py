# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list = []
for i in range(5):
    list.append(float(input('Введите данные: ')))
sum = 0
list1 = []
for i in range(len(list)):
    if round(list[i] - int(list[i]), 3) != 0:
        list1.append(abs(round(list[i] - int(list[i]), 3)))
diff = 0
diff = max(list1) - min(list1)
print(list1)
print(diff)