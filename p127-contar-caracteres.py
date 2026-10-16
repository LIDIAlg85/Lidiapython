#p127-contar-caracteres.py
# ● Escribe un programa que pida al usuario que ingrese una cadena de texto.
# ● Crea un diccionario vacío para almacenar la frecuencia (cantidad de apariciones) de cada carácter.
# ● Itera sobre cada carácter en la cadena ingresada.
# ● En cada iteración:

#borrador de pantalla de consola 
print('\033[H\033[J')

#diccionario para almacenar la frecuencia
print('Cadena de Texto')
cadena = input('Ingresa una cadena de texto: ')

frecuencia = {}
for caracter in cadena:
	if caracter in frecuencia:
		frecuencia[caracter] += 1
	else:
		frecuencia[caracter] = 1
		
# en cada interaccion
#Si el carácter no existe como llave en el diccionario, agrégalo con un valor de 1.
# #Si el carácter ya existe, incrementa su valor actual en 1.
print('Diccionario de frecuencia de cada carácter:')
print(frecuencia)
#Al finalizar el ciclo, muestra el diccionario resultante con el conteo de caracteres.
