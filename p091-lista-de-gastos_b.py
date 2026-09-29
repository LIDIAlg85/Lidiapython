##p091-lista-de-gastos_b.py

gastos = []

while True:
	print("\n--- Lista de gastos mensuales ---")
	print("1. Ver gastos")
	print("2. Agregar gasto")
	print("3. Modificar gasto")
	print("4. Eliminar gasto")
	print("5. Ver total")
	print("6. Salir")
	opcion = input("Elige una opción: ").strip()

	if opcion == "1":
		if gastos:
			for indice, gasto in enumerate(gastos, start=1):
				print(f"{indice}. ${gasto:.2f}")
		else:
			print("No hay gastos registrados.")
	elif opcion == "2":
		try:
			monto = float(input("Introduce el monto del gasto: "))
			if monto < 0:
				print("El monto no puede ser negativo.")
			else:
				gastos.append(monto)
				print("Gasto agregado correctamente.")
		except ValueError:
			print("Error: introduce un monto numérico válido.")
	elif opcion == "3":
		if not gastos:
			print("No hay gastos para modificar.")
			continue
		try:
			indice = int(input("Índice del gasto que deseas modificar: "))
			if indice < 1 or indice > len(gastos):
				print("Gasto no encontrado.")
				continue
			monto = float(input("Introduce el nuevo monto: "))
			if monto < 0:
				print("El monto no puede ser negativo.")
			else:
				gastos[indice - 1] = monto
				print("Gasto modificado correctamente.")
		except ValueError:
			print("Error: introduce números válidos.")
	elif opcion == "4":
		if not gastos:
			print("No hay gastos para eliminar.")
			continue
		try:
			indice = int(input("Índice del gasto que deseas eliminar: "))
			if indice < 1 or indice > len(gastos):
				print("Gasto no encontrado.")
			else:
				eliminado = gastos.pop(indice - 1)
				print(f"Gasto de ${eliminado:.2f} eliminado correctamente.")
		except ValueError:
			print("Error: introduce un índice numérico válido.")
	elif opcion == "5":
		print(f"Total de gastos: ${sum(gastos):.2f}")
	elif opcion == "6":
		print("Hasta luego.")
		break
	else:
		print("Opción no válida. Elige un número del 1 al 6.")
