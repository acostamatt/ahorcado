print('\n          Media Docena de Numeros')

from math import prod


numeros_ingresados = []
cantidad_de_numeros = 1

while True:
 print('\nIngrese su', cantidad_de_numeros, 'º numero.')
 un_numero = float(input())

 numeros_ingresados.append(un_numero)
 cantidad_de_numeros = cantidad_de_numeros + 1
 if len(numeros_ingresados) == 6:
     break

lista_de_numeros = sorted(numeros_ingresados)
print ('El Numero Mayor Es:', lista_de_numeros[-1])
print ('El Numero Menor Es:', lista_de_numeros[0])


print ('La Suma de Sus Numeros da:', sum(numeros_ingresados))
print ('La Multiplicacion de sus numeros da:', prod(numeros_ingresados))