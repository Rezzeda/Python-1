# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]

sp = ['ПРИВЕТ', 'ЗАБВЕНИЕ', 'ПОКА']

sp =list(filter(lambda x: 'абв' not in x.lower(), sp))

print(sp)
