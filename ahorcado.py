import os
from secrets import choice
from time import sleep
from colorama import Fore, init

os.system('clear')
print('\nBIENVENIDOS AL AHORCADO')
archivo_usuarios = open('usuarios.txt', 'a')
archivo_usuarios.close

archivo_usuarios = open('usuarios.txt', 'r')
while True:
    usuario = input('\nIngrese su nombre de usuario:').strip()
    if usuario.isdigit() is True:
        print('\nSu nombre de usuario debe constar de letras y números.')
        continue    
    elif usuario + '\n' in archivo_usuarios.readlines():
        archivo_usuarios.seek(0)
        print('\nYa se encuentra registrado ese usuario. Intente con otro nombre.')
        continue
    else:
        break
archivo_usuarios.close
os.system('clear')

archivo_usuarios = open('usuarios.txt', 'a')
archivo_usuarios.write(usuario + '\n')
palabras = open('spanish.lst', 'r')

#Inicializo la función init de colorama, para añadir color a los textos referidos a la dificultad.
init()

print('Usuario registrado correctamente.')
sleep(3)
os.system('clear')

while True:
    dificultad = input('\nSeleccione la dificultad deseada:\n'+Fore.GREEN+'Facil: F\n'+Fore.BLUE+'Normal: N\n'+Fore.RED+'Dificil: D\n\n'+Fore.WHITE+'Escriba aqui la letra que corresponda con su dificultad:  ').strip()
    palabras_para_adivinar = []    
    if dificultad.upper() == 'F':
        print('Ha seleccionado el modo Facil.')
        puntaje = 100
        palabras_para_adivinar = separador(palabras, 1, 8)
        break
    elif dificultad.upper() == 'N':
        print('Ha seleccionado el modo Normal.')
        puntaje = 200
        palabras_para_adivinar = separador(palabras, 7, 15)
        break
    elif dificultad.upper() == 'D':
        print('Ha seleccionado el modo Dificil.')        
        puntaje = 300
        palabras_para_adivinar = separador(palabras, 14, 22)
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
    
    print('\n'*7 , '_ ' * len(palabra_a_adivinar), 'Su palabra mide:', len(palabra_a_adivinar)) 
    
    while True:
        while True:
            letra = input('\nAdivina una letra: ').lower()
            os.system('clear')
            if len(letra) != 1 or letra.isnumeric():
                print('\nEso no es una letra. Intenta con una sola letra.')
                break            
            elif letra in letras_adivinadas or letra in letras_erradas:
                print('Ya intentaste con esa letra.\n')
                break            
            else:
                if letra in palabra_a_adivinar:
                    print('\nFelicitaciones ha adivinado una letra.')
                    letras_adivinadas.append(letra)
                    break
                else:
                    vidas -= 1
                    pts_por_esta_palabra -= int(puntaje/5)
                    letras_erradas.append(letra)
                    print('\nLa letra es incorrecta.')
                    break
    
        ahorcado = ahorcar(vidas)            
        if vidas == 0:
            perdiste += 1
            print(ahorcado)
            sleep(3)
            os.system('clear')
            print(f'    GAME OVER\nLa palabra era: {palabra_a_adivinar}')
            break
        
        estatus_actual = mostrar_estado(palabra_a_adivinar, letras_adivinadas)  
        letras_faltantes = faltantes(palabra_a_adivinar, letras_adivinadas)
        
        print(f'Le quedan {vidas} vidas.\n{ahorcado}')
        print('\n'*saltear_lineas_hasta_L7(vidas) + estatus_actual)
        
        if letras_faltantes == 0:
            os.system('clear')
            print('\nFelicidades haz ganado')
            print('La palabra es: ' + palabra_a_adivinar)
            puntaje_total += pts_por_esta_palabra
            print(f'Obtuvo: {pts_por_esta_palabra} pts. | Puntos acumulados: {puntaje_total} \n\n')        
            break

    if perdiste == 1:
            print(f'Su puntaje fue: {puntaje_total}')
            break

archivo_pts = open('puntajes.txt', 'a')
archivo_pts.write(f'{puntaje_total}\n')
archivo_pts.close

archivo_usuarios = open('usuarios.txt', 'r')
archivo_pts = open('puntajes.txt', 'r')
print('\n' + '-'*30)
print('Top 5 mejores puntajes')
print('-'*30)
for nombre_usuario, puntaje in select_top5_ptajes(archivo_usuarios, archivo_pts).items():
        print(str(nombre_usuario).rstrip('\n') + ' '*(20-len(nombre_usuario)) + ': ' + str(puntaje).rstrip('\n'))
        print('-'*30)
archivo_pts.close
archivo_usuarios.close