from secrets import choice
from time import sleep

print('\nBIENVENIDOS AL AHORCADO')

palabras = open('spanish.lst', 'r')
sleep(2)
while True:
    dificultad = input('\nSeleccione la dificultad deseada\nFacil: A\nNormal: B\nDificil: C\n\nEscriba aqui la letra que corresponda con su dificultad:  ')

    palabras_para_adivinar = []
    
    if dificultad.upper() == 'A':
        print('Ha seleccionado el modo Facil.')
        puntaje = 100
        for palabra in palabras.readlines():
            if len(palabra.rstrip('\n')) > 1 and len(palabra.rstrip('\n')) < 8:
                palabras_para_adivinar.append(palabra.rstrip('\n'))
        break
    
    if dificultad.upper() == 'B':
        print('Ha seleccionado el modo Normal.')
        puntaje = 200
        for palabra in palabras.readlines():
            if len(palabra.rstrip('\n')) > 7 and len(palabra.rstrip('\n')) < 15:
                palabras_para_adivinar.append(palabra.rstrip('\n'))
        break

    if dificultad.upper() == 'C':
        print('Ha seleccionado el modo Dificil.')        
        puntaje = 300
        for palabra in palabras.readlines():
            if len(palabra.rstrip('\n')) > 14 and len(palabra.rstrip('\n')) < 22:
                palabras_para_adivinar.append(palabra.rstrip('\n'))
        break

    else:
        print('Su seleccion es invalida, intente de nuevo.')

palabras.close()

print('\nAguarde mientras seleccionamos su palabra.')
sleep(2)

puntaje_total = 0
vida_4 = '|---¿\n'
vida_3 = '|   O\n'
vida_2 = '|   |\n'
vida_1 = '| --|--\n'
vida_0 = '|  J L\n'
while True:
    pts_por_esta_palabra = puntaje
    perdiste = 0
    vidas = 5
    palabra_a_adivinar = choice(palabras_para_adivinar)
    letras_adivinadas = []
    letras_erradas = []
    ahorcado = ''
    print('_ ' * len(palabra_a_adivinar))
    
    while True:
        while True:
            letra = input("Adivina una letra: ").lower()
            
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
    
        if vidas == 0:
            ahorcado = vida_4 + vida_3 + vida_1 + vida_0
            perdiste += 1
            print(ahorcado)
            print('\n    GAME OVER\nLa palabra era:', palabra_a_adivinar)
            break
        
        if vidas == 4:
            ahorcado = vida_4
        
        if vidas == 3:
            ahorcado = vida_4 + vida_3
        
        if vidas == 2:
            ahorcado = vida_4 + vida_3 + vida_2
            
        if vidas == 1:
            ahorcado = vida_4 + vida_3 + vida_1

        estatus_actual = "\n" 
        letras_faltantes = 0
        for letra in palabra_a_adivinar:
            if letra in letras_adivinadas:
                estatus_actual = estatus_actual + letra
 
            else:
                estatus_actual += "_ "
                letras_faltantes += 1   
 
        print('Le quedan', vidas, 'vidas.\n' + ahorcado, estatus_actual)
 
        if letras_faltantes == 0:
            print('\nFelicidades haz ganado')
            print('La palabra es: ' + palabra_a_adivinar)
            print('Obtuvo:', pts_por_esta_palabra, 'pts.')
            puntaje_total += pts_por_esta_palabra
            break
    
    if perdiste == 1:
            print('Su puntaje fue:', puntaje_total)
            break    