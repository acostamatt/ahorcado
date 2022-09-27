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
    return estatus_actual.upper()

def faltantes(palabra, letras_adivinadas):
    letras_faltantes = 0
    for letra in palabra:
        if letra not in letras_adivinadas:
             letras_faltantes += 1
    return letras_faltantes

def ahorcar(vidas):
    vida_4 = '┏━━━┓\n┃   ┼\n┃\n┃\n┃\n┃\n┃\n┃\n┗━━━━━━━'
    vida_3 = '┃  ┏┷┓'
    vida3_ = '┃  ┗┳┛'
    vida_2 = '┃   ┃'
    vida_1 = '┃ ━━╋━━'
    vida_0 = '┃  ┏┻┓'
    vida0_ = '┃  ┛ ┗'
    lista_lineas = vida_4.split('\n')
    global ahorcado
    if vidas == 5:
        ahorcado = vida_4
    if vidas == 4:
        lista_lineas[2] = vida_3
        lista_lineas[3] = vida3_
        ahorcado = '\n'.join(lista_lineas)
    if vidas == 3:
        lista_lineas[2] = vida_3
        lista_lineas[3] = vida3_
        lista_lineas[4] = vida_2
        ahorcado = '\n'.join(lista_lineas)
    elif vidas == 2:
        lista_lineas[2] = vida_3
        lista_lineas[3] = vida3_
        lista_lineas[4] = vida_1
        ahorcado = '\n'.join(lista_lineas)            
    elif vidas == 1:
        lista_lineas[2] = vida_3
        lista_lineas[3] = vida3_
        lista_lineas[4] = vida_1
        lista_lineas[5] = vida_0
        ahorcado = '\n'.join(lista_lineas)
    elif vidas == 0:
        ahorcado = vida_4
        lista_lineas[2] = vida_3
        lista_lineas[3] = vida3_
        lista_lineas[4] = vida_1
        lista_lineas[5] = vida_0
        lista_lineas[6] = vida0_
        ahorcado = '\n'.join(lista_lineas)
    return ahorcado

def select_top5_ptajes(bdd):
    dic_usuarios = {}
    for linea in bdd:
        usuario = linea.split(';')[0]
        puntaje = linea.split(';')[1]
        fecha = linea.split(';')[2]
        dic_usuarios[usuario] = (int(puntaje), fecha.rstrip('\n')[:16])
    puntajes_ordenados = sorted(dic_usuarios.values(), reverse=True)
    dic_top5 = {}
    for pts, fecha in puntajes_ordenados[0:5]:
        for nombre_usuario, (puntaje, fecha) in dic_usuarios.items():    
            if puntaje == pts:
                dic_top5[str(nombre_usuario)] = puntaje, fecha
            if len(dic_top5) == 5:
                break
    return dic_top5

def saltear_lineas_hasta_L12(condicion):
    if condicion == 5:
        retorno = 8
    else:
        retorno = 0
    return retorno

def validar_usuario(usuario, usuarios_en_sistema):
    global mensaje
    if str(usuario).isdigit() is True:
        mensaje = '\nSu nombre de usuario debe constar de letras y opcionalmente números.'    
    elif usuario == '':
        mensaje = '\nDebe ingresar un nombre de usuario.'
    elif len(usuario) > 19:
        mensaje = '\nSu nombre de usuario es demasiado largo. Intente con uno mas corto.'
    elif ';' in usuario:
        mensaje = '\nSu nombre de usuario no puede tener ";".'
    else:
        mensaje = ''
    for linea in usuarios_en_sistema:
        if usuario in str(linea).split(';'):
            mensaje = '\nYa se encuentra registrado ese usuario. Intente con otro nombre.'
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
