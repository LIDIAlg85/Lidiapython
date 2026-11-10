# p154-lista-pares.py
# Función  que resive una lista de numeros enteros  y me regresa  los pares de la lista

def lista_pares(lista: list[int]) -> list[int]:
	'''regresa una lista con los números pares de la lista original.'''
	pares = []
	for numero in lista:
		if numero % 2 == 0:
			pares.append(numero)

	return pares
#Programa principal
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = lista_pares(numeros)
print(f"Los números pares de la lista son: {resultado}")

