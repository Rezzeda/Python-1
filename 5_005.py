# Дан список, вывести отдельно буквы и цифры.
# a = ('1', 'a', 'b', '2', '3', 'c')
# b = ('a', 'b', 'c')
# c = ('1', '2', '3')

a = ['1', 'a', 'b', '2', '3', 'c']

c = list(filter(lambda x: x.isdigit(), a))
b = list(filter(lambda x: x.isalpha(), a))
print(b)
print(c)
