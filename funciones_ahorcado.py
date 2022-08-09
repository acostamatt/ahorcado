def dificult(palabras, n, m):
    lista_de_palabras = []
    for palabra in palabras:
            if len(str(palabra).rstrip('\n')) > n and len(str(palabra).rstrip('\n')) < m:
             lista_de_palabras.append(str(palabra).rstrip('\n'))
    return lista_de_palabras

def estatus(palabra, letras_adivinadas):
    estatus_actual = '\n'
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