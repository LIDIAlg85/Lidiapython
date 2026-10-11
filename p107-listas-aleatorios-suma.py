#p107-listas-aleatorios-suma.py
#Generar 2 listas de 10 números aleatorios cada una. 
# Crear una tercera lista donde el elemento sea la suma de los correspondientes de las listas A y B, solo si AMBOS elementos son impares;
#  de lo contrario, el elemento de la tercera lista será 0.
#  Imprimir las 3 listas.

print('\033[H\033[J')

import random

# Generar 2 listas de 10 números aleatorios cada una
lista_A = [random.randint(1, 100) for _ in range(10)]
lista_B = [random.randint(1, 100) for _ in range(10)]

# Crear una tercera lista  donde el elemento sea la suma de los correspondientes de las listas A y B, solo si AMBOS elementos son impares
# de lo contrario el elemento de la tercera lista será 0.
lista_A = [3, 4, 5, 8, 7]
lista_B = [5, 2, 9, 7, 1]
lista_C = []

for i in range(5):
    
    if lista_A[i] % 2 != 0 and lista_B[i] % 2 != 0:
        lista_C.append(lista_A[i] + lista_B[i])
    else:
        lista_C.append(0)


#Imprimir las 3 listas.
print ("\n---listas Generadas  ---")
print("Lista A:", lista_A)
print("Lista B:", lista_B)
print ("\n---Resultados ---")
print("Lista C:", lista_C)