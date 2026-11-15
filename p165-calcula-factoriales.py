#p165-calcula-factoriales.py
#Desarrolla un programa que calcule el factorial de cada número en una lista. 

#El programa debe imprimir la lista original y la lista de factoriales.


# 1. Función para leer y devolver una lista de números enteros
def leer_lista():
	entrada = input("Dame los números (separados por espacio): ")
	return [int(x) for x in entrada.strip().split() if x.strip()]

# 2. Función que recibe un número entero y devuelve su factorial
def factorial(n):
	resultado = 1
	for i in range(2, n+1):
		resultado *= i
	return resultado

# 3. Función principal que recibe la lista y devuelve la lista de factoriales
def calcula_factoriales(lista):
	return [factorial(num) for num in lista]

def main():
	numeros = leer_lista()
	factoriales = calcula_factoriales(numeros)
	print("La lista de números originales:", numeros)
	print("La lista con los factoriales:", factoriales)

if __name__ == "__main__":
	main()

