#p099-filtrar-pares.py
#Filtrar los numeros pares de una lista de introducidos usando compresion de listas 

print('\033[H\033[J')
print("\033[1;35m" + "Filtro de números pares" + "\033[0m\n")


cant= int(input('Ingrese la cantidad de numeros a Introducir: '))
numeros = []

# Se introducen numeros en la lista
for i in range(cant):
 num= int(input(f'Ingrese el número {i + 1}: '))
 numeros.append(num)

 # se filtran los numeros pares de la lista usando compresion de listas
pares = [x for x in numeros if x % 2 == 0] # par
impares = [x for x in numeros if x % 2 != 0] # impar


print(f'Los numeros Introducidos son: {numeros}')
print(f'Los numeros pares son: {pares}- cantidad de numeros pares: {len(pares)}')
print(f'Los numeros impares son: {impares}- cantidad de numeros impares: {len(impares)}')