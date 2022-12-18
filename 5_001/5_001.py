# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open("file_5_001.txt", 'r') as f:
    data = f.read().split(" ")

data = list(map(int, data))

print(data)

for i in range(1, len(data)):
    if data[i] != data[i-1] + 1:
        print(data[i-1]+1)
