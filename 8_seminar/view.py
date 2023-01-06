def show_menu():
    print('Выберите команду:\n1 - показать всех сотрудников\n2 - добавить сотрудника\n3 - изменить данные сотрудника'
          '\n4 - удалить сотрудника\n5 - экспорт в txt\n6 - импорт из txt\n7 - импорт из csv')
    try:
        select = int(input())
        if not select in [1, 2, 3, 4, 5, 6, 7]:
            raise ValueError
        return select
    except Exception:
        print("Error")
        exit()


def show_employees(spisok):
    print("Список всех сотрудников: ")
    for i, sotrudnik in enumerate(spisok):
        if i == 0:
            print(' ', *sotrudnik)
        else:
            print(i, *sotrudnik)


def add_employees():
    print("Введите Фамилию Имя Телефон и Должность через пробел: ")
    data = input().split()
    return data


def change_employees():
    print("Выберите строку для перезаписи: ")
    change = int(input())
    print('Введите строку здя записи: ')
    string = input().split()
    return change, string


def delete():
    print("Введие номер строки для удаления ")
    number = int(input())
    return number
