def pulgadas_a_centimetros(pulgadas):
	return pulgadas * 2.54


def metros_a_pies(metros):
	return metros * 3.281


while True:
	print("*** Conversor de Unidades ***")
	print("1. Pulgadas a Centímetros")
	print("2. Metros a Pies")
	print("3. Salir")

	opcion = input("Elige una opción: ")

	if opcion == "1":
		pulgadas = float(input("Introduce la cantidad en pulgadas: "))
		centimetros = pulgadas_a_centimetros(pulgadas)
		print(f"{pulgadas} pulgadas equivalen a {centimetros} centímetros.")
	elif opcion == "2":
		metros = float(input("Introduce la cantidad en metros: "))
		pies = metros_a_pies(metros)
		print(f"{metros} metros equivalen a {pies} pies.")
	elif opcion == "3":
		break
	else:
		print("Opción no válida. Inténtalo de nuevo.")

