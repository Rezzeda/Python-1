# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны.

slovar={}
slovar['Hello'] = 'Hi'
slovar['Bye'] = 'Goodbye'
slovar['List'] = 'Array'

print(slovar)
slovo=input('Введите слово, сининоним которого вы ищете: ')
for key, value in slovar.items():
    if slovo == key:
        print(value)
    elif slovo == value:
        print(key)