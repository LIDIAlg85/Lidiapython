# p135-alumnos-tuplas.py
# Registro escolar como una tupla de alumnos.

print('\033[H\033[J')

alumnos = (
	("Ana", "ISC", (9, 10, 9, 8)),
	("Luis", "ISW", (8, 8, 9, 10)),
	("Mar", "ISC", (10, 9, 10, 10)),
)

# Crear y mostrar la tupla externa con los tres registros. Imprimir cuántos alumnos contiene.
print("Registros de alumnos:", alumnos)
print(f"Total de alumnos: {len(alumnos)}")

# Recorrer los registros mediante desempaquetado y mostrar el nombre, la carrera y el promedio de cada alumno con dos decimales.
for nombre, carrera, calificaciones in alumnos:
	promedio = sum(calificaciones) / len(calificaciones)
	print(f"Nombre: {nombre}, Carrera: {carrera}, Promedio: {promedio:.2f}")

# Construir y mostrar una nueva tupla con pares (nombre, promedio). Identificar e imprimir el alumno con el promedio más alto.
promedios = tuple(
	(nombre, sum(calificaciones) / len(calificaciones))
	for nombre, carrera, calificaciones in alumnos
)
print("Pares (nombre, promedio):")
print(promedios)

alumno_destacado = max(promedios, key=lambda alumno: alumno[1])
print(f"Alumno con mejor promedio: {alumno_destacado[0]} con {alumno_destacado[1]:.2f}")

# Consultar las calificaciones usando índices de tuplas anidadas.
# Para cada alumno, mostrar cuántas veces aparece 10 con count() y el índice de la primera calificación con index().
for i in range(len(alumnos)):
	nombre = alumnos[i][0]
	calificaciones = alumnos[i][2]
	print(f"{nombre} -> Conteo de 10s: {calificaciones.count(10)}, Índice de primera calificación: {calificaciones.index(calificaciones[0])}")

# Ordenar los pares (nombre, promedio) por promedio de menor a mayor usando sorted() y mostrar el resultado como una tupla.
promedios_ordenados = tuple(sorted(promedios, key=lambda alumno: alumno[1]))
print("Ordenados por promedio:")
print(promedios_ordenados)
# Formar y mostrar una tupla nueva con Eva, sin modificar la tupla original de alumnos.
alumna_nueva = ("Eva", "ISC", (9, 9, 10))
print("Tupla original intacta:", alumnos)
alumnos_con_eva = alumnos + (alumna_nueva,)
print("Nueva tupla con Eva:", alumnos_con_eva)
