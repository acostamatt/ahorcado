import os
from secrets import choice
from time import sleep
from funciones_ahorcado import ahorcar, mostrar_estado, separador, faltantes

os.system('clear')
print('\nBIENVENIDOS AL AHORCADO')

palabras = open('spanish.lst', 'r')
sleep(2)
while True:
    dificultad = input('\nSeleccione la dificultad deseada:\nFacil: F\nNormal: N\nDificil: D\n\nEscriba aqui la letra que corresponda con su dificultad:  ').strip()

    palabras_para_adivinar = []
    
    if dificultad.upper() == 'F':
        print('Ha seleccionado el modo Facil.')
        puntaje = 100
        palabras_para_adivinar = separador(palabras.readlines(), 1, 8)
        break
    elif dificultad.upper() == 'N':
        print('Ha seleccionado el modo Normal.')
        puntaje = 200
        palabras_para_adivinar = separador(palabras.readlines(), 7, 15)
        break
    elif dificultad.upper() == 'D':
        print('Ha seleccionado el modo Dificil.')        
        puntaje = 300
        palabras_para_adivinar = separador(palabras.readlines(), 14, 22)
        break
    else:
        print('Su seleccion es invalida, intente de nuevo.')

palabras.close()

print('\nAguarde mientras seleccionamos su palabra.')
sleep(2)
os.system('clear')
puntaje_total = 0

while True:
    pts_por_esta_palabra = int(puntaje)
    perdiste = 0
    vidas = 5
    palabra_a_adivinar = choice(palabras_para_adivinar)
    letras_adivinadas = []
    letras_erradas = []
    ahorcado = ''
    
    print('_ ' * len(palabra_a_adivinar), 'Su palabra mide:', len(palabra_a_adivinar)) 
    
    while True:
        while True:
            letra = input("\nAdivina una letra: ").lower()
            os.system('clear')
            if len(letra) != 1 or letra.isnumeric():
                print("Eso no es una letra. Intenta con una sola letra.\n")
                break
            
            if letra in letras_adivinadas or letra in letras_erradas:
                print('Ya intentaste con esa letra.\n')
                break
            
            else:
                if letra in palabra_a_adivinar:
                    print('\nFelicitaciones ha adivinado una letra.')
                    letras_adivinadas.append(letra)
                    break
                else:
                    vidas -= 1
                    pts_por_esta_palabra -= puntaje/5
                    letras_erradas.append(letra)
                    print('\nLa letra es incorrecta.')
                    break
    
        ahorcado = ahorcar(vidas)            
        if vidas == 0:
            perdiste += 1
            print(ahorcado)
            print('    GAME OVER\nLa palabra era:', palabra_a_adivinar)
            break
        

        estatus_actual = mostrar_estado(palabra_a_adivinar, letras_adivinadas)  
        letras_faltantes = faltantes(palabra_a_adivinar, letras_adivinadas)
        
        print('Le quedan', vidas, 'vidas.\n' + ahorcado, '\n', estatus_actual)
        
        
        if letras_faltantes == 0:
            print('\nFelicidades haz ganado')
            print('La palabra es: ' + palabra_a_adivinar)
            
            puntaje_total += pts_por_esta_palabra
            print('Obtuvo:', pts_por_esta_palabra, 'pts.', '| Puntos acumulados:', puntaje_total, '\n\n')        
            break

    if perdiste == 1:
            print('Su puntaje fue:', puntaje_total)
            break    