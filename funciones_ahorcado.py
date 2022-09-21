def separador(palabras, desde, hasta):
    lista_filtrada = []
    for palabra in palabras:
        if len(str(palabra).rstrip('\n')) > desde and len(str(palabra).rstrip('\n')) < hasta:
            lista_filtrada.append(str(palabra).rstrip('\n'))
    return lista_filtrada

def mostrar_estado(palabra, letras_adivinadas):
    estatus_actual = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            estatus_actual += letra
        else:
             estatus_actual += "_ "
    return estatus_actual

def faltantes(palabra, letras_adivinadas):
    letras_faltantes = 0
    for letra in palabra:
        if letra not in letras_adivinadas:
             letras_faltantes += 1
    return letras_faltantes

def ahorcar(vidas):
    vida_4 = '|---¿\n'
    vida_3 = '|   O\n'
    vida_2 = '|   |\n'
    vida_1 = '| --|--\n'
    vida_0 = '|  J L\n'
    if vidas == 5:
        ahorcado = ''
    if vidas == 4:
        ahorcado = vida_4        
    if vidas == 3:
        ahorcado = vida_4 + vida_3        
    elif vidas == 2:
        ahorcado = vida_4 + vida_3 + vida_2            
    elif vidas == 1:
        ahorcado = vida_4 + vida_3 + vida_1       
    elif vidas == 0:
        ahorcado = vida_4 + vida_3 + vida_1 + vida_0    
    return ahorcado

def select_top5_ptajes(usuarios, puntajes):
    dic_usuarios = {}
    for nombre_usuario, puntaje in zip(usuarios, puntajes):
        dic_usuarios[nombre_usuario] = int(puntaje.rstrip('\n'))
    puntajes_ordenados = sorted(dic_usuarios.values(), reverse=True)
    dic_top5 = {}
    for numero in puntajes_ordenados[0:5]:
        for nombre_usuario, puntaje in dic_usuarios.items():    
            if puntaje == numero:
                dic_top5[str(nombre_usuario).rstrip('\n')] = puntaje
            if len(dic_top5) == 5:
                break
    return dic_top5

def saltear_lineas_hasta_L7(condicion):
    if condicion == 5:
        retorno = 3
    elif condicion == 4:
        retorno = 2
    elif condicion == 3:
        retorno = 1
    else:
        retorno = 0
    return retorno

def validar_usuario(usuario, usuarios_en_sistema):
    global mensaje
    if str(usuario).isdigit() is True:
        mensaje = '\nSu nombre de usuario debe constar de letras y opcionalmente números.'    
    elif usuario + '\n' in usuarios_en_sistema:
        mensaje = '\nYa se encuentra registrado ese usuario. Intente con otro nombre.'
    elif usuario is '':
        mensaje = '\nDebe ingresar un nombre de usuario.'
    else:
        mensaje = ''
    return mensaje

def select_dificultad(dificultad, palabras):
    global palabras_para_adivinar    
    global mensaje
    if str(dificultad).upper() == 'F':
        mensaje = 'Ha seleccionado el modo Facil.'
        palabras_para_adivinar = separador(palabras, 14, 22)
    elif str(dificultad).upper() == 'N':
        mensaje = 'Ha seleccionado el modo Normal.'
        palabras_para_adivinar = separador(palabras, 7, 15)
    elif str(dificultad).upper() == 'D':
        mensaje = 'Ha seleccionado el modo Dificil.'        
        palabras_para_adivinar = separador(palabras, 1, 8)
    else:
        mensaje = 'Su seleccion es invalida, intente de nuevo.'
        palabras_para_adivinar = []
    return palabras_para_adivinar, mensaje

def select_puntaje(dificultad):
    if str(dificultad).upper() == 'F':
        puntaje = 100
    elif str(dificultad).upper() == 'N':
        puntaje = 200
    elif str(dificultad).upper() == 'D':
        puntaje = 300
    else:
        puntaje = 0
    return puntaje

def validar_letra(letra, letras_adivinadas, letras_erradas):
    if len(letra) != 1 or not letra.isalpha():
        mensaje = '\nEso no es una letra. Intenta con una sola letra.'            
    elif letra in letras_adivinadas or letra in letras_erradas:
        mensaje = '\nYa intentaste con esa letra.'
    else:
        mensaje = ''
    return mensaje
