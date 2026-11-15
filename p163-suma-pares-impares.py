#p163-suma-pares-impares.py
#Crea un programa que sume números pares o impares dentro de un rango especificado. El programa debe tener una función que reciba tres parámetros: un número de inicio, un número de fin y una letra ('P' o 'I').

#Si la letra es 'P', la función debe devolver la suma de todos los números pares en ese rango (incluyendo los límites).
#Si la letra es 'I', la función debe devolver la suma de todos los números impares en el rango.
#El programa principal debe mostrar un menú, pedir los datos al usuario y mostrar el resultado de la suma.


def suma_rango(inicio, fin, tipo):
	tipo = tipo.strip().upper()
	if tipo not in ("P", "I"):
		raise ValueError("El tipo debe ser 'P' para pares o 'I' para impares.")

	paridad = 0 if tipo == "P" else 1
	limite_inferior, limite_superior = sorted((inicio, fin))
	return sum(
		numero
		for numero in range(limite_inferior, limite_superior + 1)
		if numero % 2 == paridad
	)


print("*** Suma en Rango ***")
inicio = int(input("Introduce el número inicial: "))
fin = int(input("Introduce el número final: "))
tipo = input("¿Qué deseas sumar? (P)ares o (I)mpares: ").strip().upper()

if tipo in ("P", "I"):
	nombre = "pares" if tipo == "P" else "impares"
	resultado = suma_rango(inicio, fin, tipo)
	print(f"La suma de los números {nombre} entre {inicio} y {fin} es: {resultado}")
else:
	print("Opción no válida. Debes elegir 'P' o 'I'.")
  
