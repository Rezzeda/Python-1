# Создайте программу для игры в "Крестики-нолики".
theBoard = {'1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6',
            '7': '7', '8': '8', '9': '9'}

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


turn = 'X'
count = 0

for i in range(10):
    printBoard(theBoard)
    print("\nХодит: " + turn)

    move = input('Выберите ячейку: ')

    if theBoard[move].isdigit():
        theBoard[move] = turn
        count += 1
    else:
        print("\nУже занято. Выберите другое место: ")
        continue

    if count >= 5:
        if theBoard['1'] == theBoard['2'] == theBoard['3']:
            printBoard(theBoard)
            print("\nИгра закончена.\n")
            print(" **** " + turn + " победил ****")
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6']:
            printBoard(theBoard)
            print("\nИгра закончена.\n")
            print(" **** " + turn + " победил ****")
            break
        elif theBoard['7'] == theBoard['8'] == theBoard['9']:
            printBoard(theBoard)
            print("\nИгра закончена.\n")
            print(" **** " + turn + " победил ****")
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7']:
            printBoard(theBoard)
            print("\nИгра закончена.\n")
            print(" **** " + turn + " победил ****")
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8']:
            printBoard(theBoard)
            print("\nИгра закончена.\n")
            print(" **** " + turn + " победил ****")
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9']:
            printBoard(theBoard)
            print("\nИгра закончена.\n")
            print(" **** " + turn + " победил ****")
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9']:
            printBoard(theBoard)
            print("\nИгра закончена.\n")
            print(" **** " + turn + " победил ****")
            break
        elif theBoard['7'] == theBoard['5'] == theBoard['3']:
            printBoard(theBoard)
            print("\nИгра закончена.\n")
            print(" **** " + turn + " победил ****")
            break

    if count == 9:
        print("\nИгра закончена.\n")
        print("Ничья!")

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
