# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
list=[1, 2, 2, 3, 3, 3]
new_list=[]
for i in list:
    if list.count(i)==1:
        new_list.append(i)
print(new_list)