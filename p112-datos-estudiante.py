# p112-datos-estudiante.py
# Crear un diccionario para almacenar los datos del estudiante
estudiante = {
    "nombre": "Juan Pérez",
    "edad": 28,
    "carrera": "Ingeniería de Sistemas",
    "email": "juan.perez@example.com"
}

print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")

# Modificar un dato del estudiante
estudiante["edad"] = 29
estudiante["email"] = "junito@gmail.com"

print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")

# Agregar un nuevo dato al estudiante
estudiante["promedio"] = 8.5

print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")

# Mostrar las llaves del diccionario
print("Las llaves son:")
for key in estudiante.keys():
    print(f"- {key}")

# Mostrar los valores del diccionario
print("Los valores son:")
for value in estudiante.values():
    print(f"- {value}")

# Mostrar las pares de llave-valor del diccionario
print("Los pares de llave-valor son:")
for key, value in estudiante.items():
    print(f"- {key}: {value}")
