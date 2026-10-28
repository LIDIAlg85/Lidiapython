#p134-coordenadas-tuplas.py
#Representa mediante tuplas las coordenadas de las siguientes ciudades:
# ● Zacatecas: nombre, latitud 22.77 y longitud -102.58
# ● Guadalupe: nombre, latitud 22.75 y longitud -102.52

print('\033[H\033[J')
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)
ubicaciones = (zacatecas, guadalupe)

print(f"Tupla Zacatecas: {zacatecas}, Tipo: {type(zacatecas)}")
print(f"Tupla Guadalupe: {guadalupe}, Tipo: {type(guadalupe)}")
print("Acceso por índices (Zacatecas):")
print(f"Positivos -> Nombre: {zacatecas[0]}, Latitud: {zacatecas[1]}, Longitud: {zacatecas[2]}")
print(f"Negativos -> Nombre: {zacatecas[-3]}, Latitud: {zacatecas[-2]}, Longitud: {zacatecas[-1]}")

#Desempaquetar cada tupla en variables e imprimir las coordenadas con el formato nombre: (latitud,longitud).
for ciudad in ubicaciones:
	nombre, latitud, longitud = ciudad
	print(f"{nombre}: ({latitud}, {longitud})")

#Recorrer ambas ubicaciones con un ciclo y mostrar para cada una el nombre y la tupla de coordenadas obtenida con slicing.
for ciudad in ubicaciones:
	nombre = ciudad[0]
	coordenadas = ciudad[1:]
	print(f"Ubicación: {nombre}, Coordenadas: {coordenadas}")

#Calcular e imprimir el punto medio aproximado entre las dos ubicaciones usando las latitudes y longitudes.
latitud_media = (zacatecas[1] + guadalupe[1]) / 2
longitud_media = (zacatecas[2] + guadalupe[2]) / 2
print(f"Punto medio aproximado: ({latitud_media}, {longitud_media})")

# Crear una nueva tupla para Zacatecas que incluya el código "ZAC". Mostrar la tupla nueva y comprobar que la original no cambió.
zacatecas_con_codigo = zacatecas + ("ZAC",)
print("Nueva tupla Zacatecas:", zacatecas_con_codigo)
print("Original sin cambios:", zacatecas)

#Verificar si "Zacatecas" pertenece a su tupla. En un comentario, indicar qué ocurriría si se intentara reemplazar directamente uno de sus elementos.
# Si se intentara reemplazar directamente un elemento, Python produciría un TypeError porque las tuplas son inmutables.
print('"Zacatecas" pertenece a su tupla:', "Zacatecas" in zacatecas)
