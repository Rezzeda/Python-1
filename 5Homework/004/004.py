# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# str = input('Введите текст для кодировки: ')
# with open('file1.txt', 'w') as file:
#     file.write(str)

def coding(data):
    count = 1
    result = ''
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            result = result + str(count) + data[i]
            count = 1
    if count > 1 or (data[len(data) - 2] != data[-1]):
        result = result + str(count) + data[-1]
    return result

def decoding(data):
    number = ''
    result = ''
    for i in range(len(data)):
        if data[i].isdigit():
            number += data[i]
        else:
            result = result + data[i] * int(number)
            number += str(data[i])
            number = ''
    return result


with open("file1.txt", 'r') as f:
    data = f.read()
    print(data)

print(f'Исходный текст: {data}')

with open('code.txt', 'w') as f1:
    f1.write(coding(data))

print(f'Текст после кодировки: {coding(data)}')

with open('decode.txt', 'w') as f2:
    f2.write(decoding(coding(data)))
print(f'Текст после раскодировки: {decoding(coding(data))}')