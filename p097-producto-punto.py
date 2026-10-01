# p097-producto-punto.py
## Cálculo del producto punto de dos vectores
## Cálculo del producto punto de dos vectores

vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

if len(vector1) != len(vector2):
	print("Error: los vectores deben tener la misma longitud.")
else:
	producto_punto = 0

	for i in range(len(vector1)):
		producto_punto += vector1[i] * vector2[i]

	print("El producto punto es:", producto_punto)
