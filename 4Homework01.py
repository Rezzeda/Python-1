# Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141.$ $10^{-10} ≤ d ≤10^{-1}$

import math

print(math.pi)
# Округление:
# d = float(input('Введите точность округления'))
# if (10 ** (-10)) <= d <= (10 ** (-1)):
#      print(round(math.pi, len(str(d)) - 2))
# else:
#     print('неверно задано число')

# отбрасывание ненужного:
d = (input('Введите точность округления'))
if (10 ** (-10)) <= float(d) <= (10 ** (-1)):
    print(f'{str(math.pi)[:len(d)]}')
else:
    print('неверно задано число')
