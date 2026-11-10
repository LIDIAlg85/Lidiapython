# p157-pares-impares.py
# Recibe  una lista de números y devuelva dos listas: una con los números pares y otra con los impares.


def separar_pares_impares(lista: list[int]) -> tuple[list[int], list[int]]:
	'''Separa los números pares y otra con los impares de la lista original y regresa 2 listas.'''
	pares = []
	impares = []
	for numero in lista:
		if numero % 2 == 0:
			pares.append(numero)
		else:
			impares.append(numero)

	return pares, impares

# Programa principal
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar_pares_impares(numeros)
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")