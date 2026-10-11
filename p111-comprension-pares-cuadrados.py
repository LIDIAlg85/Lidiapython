#p111-comprension-pares-cuadrados.py
#Generar una lista de números enteros del 1 al n (donde n es ingresado por el usuario).
#Utilizando comprensión de listas, obtener una nueva lista que contenga los cuadrados únicamente de los números pares.
#  Imprimir la lista con el rango completo, la lista resultante de cuadrados y la suma de dichos cuadrados.

print('\033[H\033[J')

#Generar una lista de números enteros del 1 al n 
n = int(input("Introduzca el limite n: "))

#Utilizando comprensión de listas,
numeros = list(range(1, n + 1))
cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]
suma_cuadrados_pares = sum(cuadrados_pares)

#Imprimir la lista con el rango completo
print("\n---Resultados ---")
print("Lista Original:", *numeros)
print("Cuadrados de numeros paes:", *cuadrados_pares)
print("Suma de los cuadrados:", suma_cuadrados_pares)
