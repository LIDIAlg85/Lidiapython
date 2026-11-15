#p161-dia-semana.py
#Escribe un programa con una función que reciba un número entero entre 1 y 7. La función debe devolver el día de la semana correspondiente en texto (ej: 1 = "Lunes", 7 = "Domingo"). El programa principal debe pedir el
#número al usuario, llamar a la función y mostrar el nombre del día.


def dia_de_la_semana(numero):
	dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
	if 1 <= numero <= 7:
		return dias[numero - 1]
	return None


numero = int(input("Introduce un número del 1 al 7: "))
dia = dia_de_la_semana(numero)

if dia is None:
	print("Error: El número debe estar entre 1 y 7.")
else:
	print(f"El día es: {dia}")
