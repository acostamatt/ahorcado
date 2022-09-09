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