# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import re

#метод кот. достает числа из уравнений в файле и разворачивает в порядке возр. степени
def extract_koef(data):
    list1 = []
    for element in data:
        value = re.findall(r"[-+]?\d*\.\d+|\d+", element)
        if value != [] and value != ['0']:
            list1.append(value[0])
    list1.reverse()
    return list1

# с помощью метода достаем числа
with open("mnogochlen1.txt", 'r') as f:
    data = f.read().split(" ")
    # print(data)

koef1 = extract_koef(data)
# print(koef1)

with open("mnogochlen2.txt", 'r') as f2:
    data2 = f2.read().split(" ")
    # print(data2)
koef2 = extract_koef(data2)
# print(koef2)

# учитываем условие количества коэффициентов:
for i in range(max(len(koef1), len(koef2))):
    if len(koef1) < len(koef2):
        koef1.append(0)

    elif len(koef1) > len(koef2):
        koef2.append(0)

# print(koef1)
# print(koef2)

#Находим сумму к-тов согласно их степени
sum_koef = []
for i in range(len(koef1)):
    sum_koef.append(int(koef1[i]) + int(koef2[i]))
# print(sum_koef)
# разворачиваем чтоб коэф-ты шли по убыванию степени
sum_koef.reverse()
# print(sum_koef)

# подставляем в многочлен
uravnen = ''
k = len(sum_koef)
while k > 1:
    for i in range(k - 1):
        uravnen = uravnen + f' {sum_koef[i]}x**{k} +'
        k -= 1
    break
print(f'{uravnen} {sum_koef[-1]} = 0')

# записываем в новый файл
with open('mnogochlen_sum.txt', 'w') as file:
    file.write(f'{uravnen} {sum_koef[-1]} = 0')
