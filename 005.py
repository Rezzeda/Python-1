#Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

number=int(input(('введите число')))

if(number%30!=0 and (number%5==0 and number%10==0 or number%15==0)):
    print('кратно 5 и 10 или 15, но не 30')
else:
    print('нет')