#p166-estadisticas-basicas.py
#Crea un programa que calcule estadísticas básicas (poblacionales) para una lista de números. El programa debe incluir:
# 1. Una función para leer una lista de números enteros.
# 2. Funciones separadas para calcular y devolver cada una de las siguientes estadísticas:
# o Número mayor
# o Número menor
# o Media (promedio)
# o Varianza poblacional
# o Desviación estándar poblacional

def leer_lista():
	entrada = input("Dame números (separados por espacio): ")
	return [int(x) for x in entrada.strip().split()]

def calcular_mayor(lista):
	return max(lista)

def calcular_menor(lista):
	return min(lista)

def calcular_media(lista):
	return sum(lista) / len(lista)

def calcular_varianza(lista):
	media = calcular_media(lista)
	return sum((x - media) ** 2 for x in lista) / len(lista)

def calcular_desviacion(lista):
	import math
	return math.sqrt(calcular_varianza(lista))

def imprimir_estadisticas(lista):
	media = calcular_media(lista)
	mayor = calcular_mayor(lista)
	menor = calcular_menor(lista)
	varianza = calcular_varianza(lista)
	desviacion = calcular_desviacion(lista)
	print(f"Lista de números: {lista}")
	print("Estadísticas:")
	print(f"Media : {media:.3f}")
	print(f"Mayor : {mayor}")
	print(f"Menor : {menor}")
	print(f"Varianza : {varianza:.3f}")
	print(f"Desviación estándar: {desviacion:.3f}")

if __name__ == "__main__":
	lista = leer_lista()
	imprimir_estadisticas(lista)
