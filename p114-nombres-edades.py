 # p114-nombres-edades.py
# Censo de nombres y edades en un diccionario, hasta <Enter> vacío

# borrar la consola
print("\033c", end="")

# Crear un diccionario para almacenar los nombres y edades
censo = {}

# Solicitar al usuario que ingrese nombres y edades hasta que ingrese
# un nombre vacío
while True:
	nombre = input("Ingrese un nombre (o presione <Enter> para salir):\n")
	if nombre == "":
		break
	censo[nombre] = int(input(f"Ingrese la edad de {nombre}: "))

# Mostrar el censo de nombres y edades
print(f"Censo de nombres y edades: {censo} → {len(censo)} elementos")

 # Resumen  del senso
print("\nResumen del censo:")
for nombre, edad in censo.items():
    print(f"- {nombre}: {edad} años")

print()

suma_edades = sum(censo.values())  # suma todas las edades
promedio_edades = suma_edades / len(censo) if censo else 0
print(f"Suma de edades: {suma_edades} años")
print(f"Promedio de edades: {promedio_edades:.2f} años")

