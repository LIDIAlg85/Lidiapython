# p160–numero-menor.py
#Crea un programa que incluya una función. Dicha función debe solicitar 3 números enteros al usuario y devolver el menor.


def obtener_menor():
	primer_numero = int(input("Introduce el primer número: "))
	segundo_numero = int(input("Introduce el segundo número: "))
	tercer_numero = int(input("Introduce el tercer número: "))
	return min(primer_numero, segundo_numero, tercer_numero)


print(f"El número menor es: {obtener_menor()}")


