#p108-ciudades.py
#Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $. Imprimir:
#Cuántos elementos tiene la lista.
#La lista completa.
#La lista ordenada en orden descendente.
#Cuántas ciudades inician con una letra consonante y sus nombres.

print('\033[H\033[J')

#Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $. Imprimir:
ciudades = []
while True:
    ciudad = input("Introduce el nombre de una ciudad ('$' para terminar): ")
    if ciudad == '$':
        break
    ciudades.append(ciudad)
#Cuántos elementos tiene la lista.
lista_descendente = ciudades.copy()
lista_descendente.sort()  # Ordena de A a Z
lista_descendente = lista_descendente[::-1]  # Voltea la lista (de Z a A)

print("\n--- Resultados ---")
print(f"\nTotal de Ciudades Introducidas: {len(ciudades)}")
print(f"\nLa lista Original: {ciudades}")
print(f'\nLa lista ordenada en orden descendente: {lista_descendente}')


consonantes = "bcdfghjklmnpqrstvwxyz"
count_consonantes = 0
nombres_consonantes = []

for ciudad in ciudades:
    if ciudad[0].lower() in consonantes:
        count_consonantes += 1
        nombres_consonantes.append(ciudad)


print(f"\nCuántas ciudades inician con una letra consonante: {count_consonantes}")
print(f" \nSus nombres: {nombres_consonantes}")
