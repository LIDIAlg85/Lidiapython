##p091-lista-de-gastos.py
#Desarrolla una aplicación que almacene gastos en una lista y permita al usuario manipularla a través de un menú que se mostrará continuamente hasta que decida salir.

gastos = []

def mostrar_menu():
	while True:
		print('\033[H\033[J')
		print("\n--- Lista de gastos ---")
		print("1. Añadir gasto")
		print("2. Mostrar gastos")
		print("3. Eliminar gasto")
		print("4. Modificar gasto")
		print("5. Mostrar total")
		print("6. Salir")

		opcion = input("Elige una opción: ").strip()

		if opcion == "1":
			descripcion = input("Descripción del gasto: ").strip()
			if not descripcion:
				print("La descripción no puede estar vacía.")
				continue
			try:
				importe = float(input("Importe: ").replace(",", "."))
				if importe < 0:
					print("El importe no puede ser negativo.")
					continue
			except ValueError:
				print("Introduce un importe válido.")
				continue
			gastos.append({"descripcion": descripcion, "importe": importe})
			print("Gasto añadido.")

		elif opcion == "2":
			if not gastos:
				print("No hay gastos registrados.")
			else:
				for indice, gasto in enumerate(gastos, start=1):
					print(f"{indice}. {gasto['descripcion']}: {gasto['importe']:.2f}")

		elif opcion == "3":
			if not gastos:
				print("No hay gastos para eliminar.")
				continue
			try:
				indice = int(input("Número del gasto que quieres eliminar: "))
				if not 1 <= indice <= len(gastos):
					print("Ese número no corresponde a un gasto.")
					continue
				eliminado = gastos.pop(indice - 1)
				print(f"Gasto '{eliminado['descripcion']}' eliminado.")
			except ValueError:
				print("Introduce un número válido.")

		elif opcion == "4":
			if not gastos:
				print("No hay gastos para modificar.")
				continue
			try:
				indice = int(input("Número del gasto que quieres modificar: "))
				if not 1 <= indice <= len(gastos):
					print("Ese número no corresponde a un gasto.")
					continue
				descripcion = input("Nueva descripción: ").strip()
				importe = float(input("Nuevo importe: ").replace(",", "."))
				if not descripcion or importe < 0:
					print("La descripción no puede estar vacía y el importe no puede ser negativo.")
					continue
				gastos[indice - 1] = {"descripcion": descripcion, "importe": importe}
				print("Gasto modificado.")
			except ValueError:
				print("Introduce datos válidos.")

		elif opcion == "5":
			total = sum(gasto["importe"] for gasto in gastos)
			print(f"Total de gastos: {total:.2f}")

		elif opcion == "6":
			print("Hasta pronto.")
			break

		else:
			print("Opción no válida. Elige una opción del 1 al 6.")


mostrar_menu()

