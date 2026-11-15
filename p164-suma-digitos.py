# p164-suma-digitos.py
#Escribe un programa que procese una lista de números. Debes implementar lo siguiente:
# Una función que lea y devuelva una lista de números enteros (puedes reusar la hecha en clase).
# Una función que reciba un número entero y devuelva la suma de sus dígitos individuales (ej: 1971 -> 1+9+7+1 = 18).
# Una función principal que reciba la lista de números. Esta debe usar la función anterior para crear y
# devolver una nueva lista que contenga la suma de los dígitos de cada número original.
# El programa debe imprimir la lista original y la nueva lista con las sumas.


def leer_numeros():
	"""Lee números separados por espacios y devuelve una lista de enteros."""
	return [int(numero) for numero in input("Dame los números (separados por espacio): ").split()]


def suma_digitos(numero):
	"""Devuelve la suma de los dígitos de un número entero."""
	return sum(int(digito) for digito in str(abs(numero)))


def sumar_digitos_lista(numeros):
	"""Devuelve una lista con la suma de los dígitos de cada número."""
	return [suma_digitos(numero) for numero in numeros]


def main():
	numeros = leer_numeros()
	sumas = sumar_digitos_lista(numeros)
	print("La lista de números original :", numeros)
	print("La lista con las suma de dígitos de los números:", sumas)


if __name__ == "__main__":
	main()
