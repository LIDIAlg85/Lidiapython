#p158-aleatorios.py
#Funcion que genera lista de numeros aleatorios 
# luego genero 2 listas aleatorias usando esa funcion 
# luego obtengo la suma de ambas con otra funcion

import random

def generaAleatoria(n: int, minimo: int, maximo: int) -> list[int]:
    '''Genera una lista de n números aleatorios entre minimo y maximo.'''
    lista = []
    for _ in range(n):
        numero= random.randint(minimo, maximo)
        lista.append(numero)
    return lista

def sumar_listas(lista1: list[int], lista2: list[int]) -> list[int]:
    '''Suma los elementos de dos listas y regresa una nueva lista con los resultados.'''

    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud")
    suma = []
    for i in range(len(lista1)):
        suma.append(lista1[i] + lista2[i])
    return suma

#Programa principal
MAX=10
lista1 = generaAleatoria(MAX, 1, 10)
lista2 = generaAleatoria(MAX, 50, 100)
lista3 = sumar_listas(lista1, lista2)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
if lista3==0:
    print("La lista no tiene la misma longitud,no se puede sumar.")
else:    
 print(f"Suma de listas: {lista3}")