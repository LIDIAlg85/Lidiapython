print("\033c", end="")

# Crear dos listas, una de materias otra de calificaciones
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua", "Inglés"]
calificaciones = [8.5, 9.0, 7.5, 6.0, 8.0, 9.5]

# Crear un diccionario para almacenar las calificaciones del estudiante
calificaciones_estudiante = dict(zip(materias, calificaciones))

# Mostrar las calificaciones del estudiante
print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")

# Agregar dos nuevas calificaciones al estudiante
calificaciones_estudiante["Educación Física"] = 10.0
calificaciones_estudiante["Arte"] = 9.0

print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")

# Actualizar 3 calificaciones del estudiante
calificaciones_estudiante["Matemáticas"] = 9.0
calificaciones_estudiante["Física"] = 8.5
calificaciones_estudiante["Historia"] = 7.0

print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")

# Eliminar 2 calificaciones del estudiante usando pop
calificaciones_estudiante.pop("Química")
calificaciones_estudiante.pop("Inglés")

print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")

# Mostrar cada materia con su calificación, sumar calificaciones y calcular el promedio
print("\nValores de las calificaciones del estudiante:")
total = 0

for materia, calificacion in calificaciones_estudiante.items():
    print(f"- {materia}: {calificacion}")
    total += calificacion

promedio = total / len(calificaciones_estudiante)
print(f"Promedio de calificaciones: {promedio:.2f}")


