# #Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите значение X: "))
y = int(input("Введите значение Y: "))
z = int(input("Введите значение Z: "))

left = not (x or y or z)
right = not x and not y and not z

print(left)
print(right)
if (left == right):
    print("Утверждение истинно")
else:
    print("Утверждение ложно")