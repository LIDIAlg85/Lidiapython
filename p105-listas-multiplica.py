#p105-listas-multiplica.py
# Leer 2 listas, cada una con 5 elementos numéricos.
# Crear una tercera lista multiplicando los elementos de las dos listas correspondientes.
# Imprimir las tres listas.

print('\033[H\033[J')
# leer 2 listas con 5 elementos numericos cada una 
lista_A = [2, 4, 6, 8, 10]
lista_B = [5, 1, 3, 7, 9]

print("Introduzca 5 números para la Lista A:", *lista_A)
print("Introduzca 5 números para la Lista B:", *lista_B)

# Crear una tercera lista multiplicando los elementos de las dos listas correspondientes.
lista_C = []
for i in range(5):
    lista_C.append(lista_A[i] * lista_B[i])

# Imprimir las tres listas.
print("\n--- Resultados ---")
print(f"Lista A: {lista_A}")
print(f"Lista B: {lista_B}")
print(f"Lista C (A * B): {lista_C}")

