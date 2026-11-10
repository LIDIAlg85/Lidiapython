# p159-nombres.py
# Función que tome dos listas de nombres y regresa una lista las una,
# 1.nombres  que estan en ambas listas 
# 2.invier la lista
# 3.convierta a mayúsculas.


def capturadenombres() -> list[str]:
	'''Captura una lista de nombres del usuario .'''
	nombres = []
	while True:
		nombre = input("Nombre (o deja en blanco para terminar): ")
		if nombre == "":
			break
		nombres.append(nombre)
	return nombres

def procesanombres(lista1:list[str], lista2:list[str]) -> list[str]:
	'''Regresa una lista con los nombres que están en ambas listas, invertidos y en mayúsculas.'''
	todos= lista1 + lista2
	invertidos = todos[::-1]
	nombres_mayusculas = [nombre.upper() for nombre in invertidos]
	mayusculas = []
	for i in range(len(invertidos)):
		mayusculas.append(invertidos[i].upper())
	return mayusculas

nombres1 = ["Ana", "Luis", "Carlos", "Marta", "María"]
nombres2 = capturadenombres()
nombres_procesados = procesanombres(nombres1, nombres2)
print(f"Nombres de la primera lista son: {nombres1}")
todos=procesanombres(nombres1, nombres2)
print(f"Nombres de ambas listas,invertidos y en mayusculas son: {todos}")