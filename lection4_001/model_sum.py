#модель с данными, с которыми работаем, их инициализатор и логика работы

x = 0
y = 0


def init(a, b):
    global x
    global y
    x = a
    y = b


def do_it():
    return x + y
