# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
import re

stroka = input("Введите строку: ")


def coding(data):
    count = 1
    result = ''
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            result = result + ' ' + str(count) + data[i]
            count = 1
    if count > 1 or (data[len(data) - 2] != data[-1]):
        result = result + ' ' + str(count) + data[-1]
    result = list(result.split(' '))
    return result


res = coding(stroka)

list = [int(res[i][:-1]) for i in range(1, len(res)) if res[i][-1] == 'Р']

if list == []:
    print('0')
else:
    kol = max(list)
    print(kol)
