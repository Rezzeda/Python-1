# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint

player1 = input('Введите имя первого игрока: ')
player2 = 'БОТ'
value = int(input('Введите количество конфет: '))

def input_dat(name):
    x = int(input(f'{name}, введите количество конфет, которое возьмете от 1 до 28: '))
    while x < 1 or x > 28:
        x = int(input(f'{name}, введите корректное количество конфет: '))
    return x


def p_print(name, k, value):
    print(f'{name} взял(а) {k} конфет. Осталось {value} конфет(ы).')

def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

flag = randint(0,2) # флаг очередности
if flag:
    print(f'Первый ходит: {player1}')
else:
    print(f'Первый ходит: {player2}')

while value > 28:
    if flag:
        k = input_dat(player1)
        value -= k
        flag = False
        p_print(player1, k, value)
    else:
        k = bot_calc(value)
        value -= k
        flag = True
        p_print(player2, k, value)

if flag:
    print(f'{player1} вы выиграли!')
else:
    print(f'{player2} выиграл!')
