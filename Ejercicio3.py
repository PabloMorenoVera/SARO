#!/usr/bin/python3

diccionario = {'red':'rojo', 'green':'verde', 'blue':'azul', 'pink':'rosa', 'white':'blanco'}

for translate in diccionario:
    print(translate, ':', diccionario[translate])

print("\nOtra forma:\n")

for key, value in diccionario.items():
    print (key + ':' + value)
