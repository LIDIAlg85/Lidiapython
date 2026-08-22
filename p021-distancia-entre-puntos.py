#p021-distancia-entre-puntos.py
#Crea un programa que calcule la distancia entre dos puntos en un plano cartesiano
## Formula d = √((x2 - x1)² + (y2 - y1)²)


import math as mt
print("\033[2J\033[1;1H",end="")



print("=== CALCULAR LA DISTANCIA ENTRE DOS PUNTOS ===")


x1 = float(input("Ingresa la coordenada x1 para el Punto A: "))
y1 = float(input("Ingresa la coordenada y1 para el Punto A: "))


x2 = float(input("Ingresa la coordenada x2 para el Punto B: "))
y2 = float(input("Ingresa la coordenada y2 para el Punto B: "))



distancia = mt.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print("\n= RESULTADO =")
print(f"Punto A: ({x1}, {y1})")
print(f"Punto B: ({x2}, {y2})")
print(f"La distancia entre los dos puntos es: {distancia:.2f}")