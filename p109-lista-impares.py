#p109-lista-impares.py
#Leer un entero n. Llenar una lista con los primeros n números impares.Calcular e imprimir:
#● La suma y el promedio de los números.
#● Los números que son divisibles entre 3 y su suma.
#● Pedir un elemento a buscar en la lista original e indicar si está y en qué posición (índice).

print('\033[H\033[J')

n = int(input("Itrodusca la cantidad de numeros impares(n) : "))


# 2. Llenar la lista con los primeros n números impares
impares = []
numero = 1
while len(impares) < n:
    impares.append(numero)
    numero += 2

print("\n--- Generacion de listas ---")
print("Lista de  los primeros 6 numeros impares:", *impares)

# 3. Calcular e imprimir la suma y el promedio de los números
suma_total = sum(impares)
promedio = suma_total / len(impares) if len(impares) > 0 else 0

print("\n--- Cálculos Generales ---")
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio:.2f}")

# 4. Los números que son divisibles entre 3 y su suma
divisibles_3 = [num for num in impares if num % 3 == 0]
suma_divisibles_3 = sum(divisibles_3)

print("\n--- Divisibles entre 3 ---")
print("Números divisibles entre 3:", *divisibles_3)
print(f"Suma de divisibles entre 3: {suma_divisibles_3}")

# 5. Pedir un elemento a buscar en la lista original
print ("\n---Busqueda  ---")
buscar = int(input("\nIntroduce el número que deseas buscar en la lista: "))

if buscar in impares:
    posicion = impares.index(buscar)
    print(f"El número {buscar} SÍ está en la lista, en la posición (índice): {posicion}")
else:
    print(f"El número {buscar} NO se encuentra en la lista.")



