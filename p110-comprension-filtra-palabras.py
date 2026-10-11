#p110-comprension-filtra-palabras.py
#Dada una lista de palabras introducidas por el usuario separadas por espacios, utilizar comprensión de listas
#para crear una nueva lista que contenga solo aquellas palabras que tengan más de 4 caracteres y convertirlas a mayúsculas.
#Imprimir la lista original y la lista filtrada.

print('\033[H\033[J')
# Leer una lista de palabras introducidas por el usuario separadas por espacios
palabras = input("Introduzca palabras separadas por espacios: ").split()

# Utilizar comprensión de listas para crear una nueva lista con palabras de más de 4 caracteres en mayúsculas
palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 4]

# Imprimir la lista original y la lista filtrada
print ("\n---Resultados ---")
print("Lista original:", *palabras)
print("Lista filtrada:", *palabras_filtradas)
