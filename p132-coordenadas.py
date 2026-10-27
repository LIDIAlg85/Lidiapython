# p132-coordenadas.py
# coordenadas como tuplas
# Registro de coordenadas
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)
ubicaciones = (zacatecas, guadalupe)

print("--- Coordenadas ---")
print("Tipo:", type(zacatecas))

# Consultar valores mediante índices y desempaquetado
print("Ciudad:", zacatecas[0])
print("Latitud:", zacatecas[1])
print("Longitud:", zacatecas[2])

nombre, latitud, longitud = zacatecas
print(f"{nombre}: ({latitud}, {longitud})")

# Recorrer las ubicaciones sin modificar las tuplas
for lugar in ubicaciones:
	print(lugar[0], "->", lugar[1:])

# Desenpaquetar coordenadas
_, lat1, lon1 = zacatecas
_, lat2, lon2 = guadalupe

# Calcular el punto medio aproximado
centro = ((lat1 + lat2) / 2, (lon1 + lon2) / 2)
print("Punto medio:", centro)

# Crear una tupla con datos extra 
ampliada = zacatecas + ("ZAC",)
print("Ampliada:", ampliada)
print("Original:", zacatecas)