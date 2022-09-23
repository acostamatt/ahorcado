from os import system
from secrets import choice
from time import sleep
from pyfiglet import figlet_format
from colorama import Fore, init
from funciones_ahorcado import saltear_lineas_hasta_L12, select_dificultad, select_puntaje, select_top5_ptajes, separador, ahorcar, mostrar_estado, faltantes, validar_letra, validar_usuario
#TITULO
system('clear')
init()
print(f'\n{Fore.MAGENTA}{figlet_format("BIENVENIDOS AL  AHORCADO")}{Fore.WHITE}')
archivo_usuarios = open('usuarios.txt', 'a')
archivo_usuarios.close
#IGRESO DE USUARIO
archivo_usuarios = open('usuarios.txt', 'r')
while True:
    usuario = input('\nIngrese su nombre de usuario: ').strip()
    system('clear')
    print(f'\n{Fore.MAGENTA}{figlet_format("BIENVENIDOS AL  AHORCADO")}{Fore.WHITE}')
    mensaje_validacion = validar_usuario(usuario, archivo_usuarios)
    archivo_usuarios.seek(0)
    print(mensaje_validacion)
    if len(mensaje_validacion) == 0:
        break
archivo_usuarios.close
system('clear')
print(f'{Fore.MAGENTA}Usuario registrado correctamente.{Fore.WHITE}')
sleep(2)
system('clear')
#SE SELECCIONA LA DIFICULTAD
palabras = open('spanish.lst', 'r')
while True:
    dificultad = input('\nSeleccione la dificultad deseada:\n'+Fore.GREEN+'Facil: F\n'+Fore.YELLOW+'Normal: N\n'+Fore.RED+'Dificil: D\n\n'+Fore.WHITE+'Escriba aqui la letra que corresponda con su dificultad:  ').strip()
    system('clear')
    palabras_para_adivinar = select_dificultad(dificultad, palabras)[0]
    mensaje_dificultad = select_dificultad(dificultad, palabras)[1]
    puntaje = select_puntaje(dificultad)
    print(mensaje_dificultad)
    if len(palabras_para_adivinar) != 0:
        break
palabras.close()
sleep(2)
system('clear')
#SE SELECCIONA LA PALABRA A ADIVINAR POR AZAR
puntaje_total = 0
while True:
    pts_por_esta_palabra = int(puntaje)
    perdiste = 0
    vidas = 5
    palabra_a_adivinar = choice(palabras_para_adivinar)
    letras_adivinadas = []
    letras_erradas = []
    ahorcado = ''
    print('Aguarde mientras seleccionamos su palabra.')
    sleep(2)
    system('clear')
    #SE LE MUESTRA AL USUARIO LA CANTIDAD DE LETRAS DE LA PALABRA
    print('\n'*12 , '_ ' * len(palabra_a_adivinar), 'Su palabra contiene', len(palabra_a_adivinar), 'letras') 
    while True:
        #INGRESO Y VALIDACION DE LETRAS 
        while True:
            letra = input('\nAdivina una letra: ').lower()
            system('clear')
            mensaje_valid_letra = validar_letra(letra, letras_adivinadas, letras_erradas)
            print(mensaje_valid_letra)
            if len(mensaje_valid_letra) == 0:    
                if letra in palabra_a_adivinar:
                    print('Felicitaciones ha adivinado una letra.')
                    letras_adivinadas.append(letra)
                    break
                else:
                    vidas -= 1
                    pts_por_esta_palabra -= int(puntaje/5)
                    letras_erradas.append(letra)
                    print('La letra es incorrecta.')
                    break
            else:
                break
        #MUESTRA DE ESTADO DE LA PALABRA Y DE VIDAS
        ahorcado = f'{Fore.RED}{ahorcar(vidas)}{Fore.WHITE}'
        estatus_actual = f'{Fore.GREEN}{mostrar_estado(palabra_a_adivinar, letras_adivinadas)}{Fore.WHITE}'
        letras_faltantes = faltantes(palabra_a_adivinar, letras_adivinadas)        
        mensaje_vidas = (f'Le quedan {vidas} vidas.\n{ahorcado}')
        if vidas == 1:
            print((mensaje_vidas.replace('quedan', 'queda')).replace('vidas', 'vida'))
        else:
            print(mensaje_vidas)
        print(f' {estatus_actual} Su palabra contiene {len(palabra_a_adivinar)} letras')
        #VALIDACION SI EL USUARIO ADIVINO
        if letras_faltantes == 0:
            system('clear')
            print(f'\n{Fore.GREEN}¡Felicidades adivinaste!')
            print('La palabra es: ' + str(palabra_a_adivinar).upper())
            puntaje_total += pts_por_esta_palabra
            print(f'Obtuvo: {pts_por_esta_palabra} pts. | Puntos acumulados: {puntaje_total}{Fore.RESET}')
            sleep(4)
            system('clear')
            break
        #VALIDACION DE VIDAS
        if vidas == 0:
            system('clear')
            perdiste += 1
            print(ahorcado)
            sleep(5)
            system('clear')
            print(f'{Fore.RED}{figlet_format("GAME   OVER")}{Fore.WHITE} \nLa palabra era: {str(palabra_a_adivinar).upper()}')
            break
    #VALIDACION SI EL USUARIO PERDIO
    if perdiste == 1:
            print(f'Su puntaje fue: {Fore.CYAN}{puntaje_total}')
            break
#SE AGREGA EL PUNTAJE AL SISTEMA DE USUARIOS
archivo_usuarios = open('usuarios.txt', 'a')
archivo_usuarios.write(usuario + '\n')
archivo_usuarios.close
archivo_pts = open('puntajes.txt', 'a')
archivo_pts.write(f'{puntaje_total}\n')
archivo_pts.close
#SE MUESTRA AL USUARIO LOS MEJOR 5 PUNTAJES EN EL SISTEMA DE PUNTAJES
archivo_usuarios = open('usuarios.txt', 'r')
archivo_pts = open('puntajes.txt', 'r')
print(Fore.LIGHTMAGENTA_EX + '\n' + '-'*30)
print('Top 5 mejores puntajes')
print('-'*30)
for nombre_usuario, puntaje in select_top5_ptajes(archivo_usuarios, archivo_pts).items():
        print(str(nombre_usuario).rstrip('\n') + ' '*(20-len(nombre_usuario)) + ': ' + Fore.CYAN + str(puntaje).rstrip('\n') + Fore.LIGHTMAGENTA_EX)
        print('-'*30)
archivo_pts.close
archivo_usuarios.close