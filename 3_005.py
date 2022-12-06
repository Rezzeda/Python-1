# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# например	список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
element = "qwe"
count = 0
for i in range(len(list)):
    if list[i] == element:
        count += 1
    if count == 2:
            print(i)
            break
if count < 2:
    print(-1)
# if any(element for i in list):
#     print(f'Да{list[i]}')
