import random


print('\n       Parcial')

archivo = open('spanish.lst','r')
lineas = archivo.readlines()
palabras_sin_enter = ''.join(lineas)
palabras = palabras_sin_enter.split('\n')

letrasXpalabra = []
for palabra in palabras:
    letrasXpalabra.append(len(palabra))
promedio = sum(letrasXpalabra) / len(palabras)

palabras_a_ordenar = []
for palabra in palabras:
    palabras_a_ordenar.append((len(palabra), palabra))
palabras_ordenada = sorted(palabras_a_ordenar)
palabra_mas_larga = palabras_ordenada[-1][1]

print('\nLa cantidad de palabras del diccionario es:', len(lineas))
print('El promedio de cantidad de letras por palabra es:', str(promedio)[0:4])
print('La palabra mas larga es:', '\n', str(palabra_mas_larga).upper(), 'Y tiene', len(palabras_ordenada[-1][1]), 'letras.')

while True:
    try:
        cantidad_de_palabras = int(input('\nIngrese un numero o si desea terminar escriba 0:'))
    except:
        print('Su ingreso es incorrecto, intente de nuevo.')
        continue
    else:
        if cantidad_de_palabras == 0:
            break
    
    palabras_random = []
    for palabra in palabras:
        if len(palabra) == cantidad_de_palabras:
            palabras_random.append(palabra.upper())

    try:
        print('; '.join(random.sample(palabras_random, 20)))
    except:
        print('\nNo hay 20 palabras con esa cantidad de letras.')
        if len(palabras_random) < 20:
            print('; '.join(palabras_random))
        if len(palabras_random) == 0:
            print('No hay palabras con esa cantidad de letras.')
    else:
        continue

archivo.close