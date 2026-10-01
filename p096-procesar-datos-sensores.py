#p096-procesar-datos-sensores.py
# Planteamiento del problema: Procesamiento de datos de sensores
#Se tienen dos sensores que recogen 10 mediciones numéricas cada uno.
#Necesitamos un programa que realice las siguientes tareas:

from random import randint


print('\033[H\033[J')

sensor_1 = []
sensor_2 = []

# Genere dos listas con 10 números aleatorios (entre 1 y 100) para simular los datos de cada sensor y las muestre.
mediciones = 10
for _ in range(mediciones):
    sensor_1.append(randint(1, 100))
    sensor_2.append(randint(1, 100))

print("Datos del Sensor 1:", sensor_1)
print("Datos del Sensor 2:", sensor_2)

#Aplique una "transformación" a los datos, que consiste en elevar al cuadrado cada medición en ambas listas.
sensor_1_cuadrado = [x**2 for x in sensor_1]
sensor_2_cuadrado = [x**2 for x in sensor_2]

print("Datos del Sensor 1 (al cuadrado):", sensor_1_cuadrado)
print("Datos del Sensor 2 (al cuadrado):", sensor_2_cuadrado)

# Cree una tercera lista que contenga la suma combinada de los datos transformados de ambos sensores (la suma del primer elemento de la lista 1 con el primero de la lista 2, y así sucesivamente).
lista_combinada = [a + b for a, b in zip(sensor_1_cuadrado, sensor_2_cuadrado)]
print("Suma combinada de los datos transformados:", lista_combinada)
