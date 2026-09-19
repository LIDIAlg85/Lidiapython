#p082-cuadro-hueco-caracter.py
# Ingrese el tamaño del lado de un cuadrado y el carácter con el que se dibujara.

print("\033[H\033[J")
print("Ingrese el tamaño del lado de un cuadrado y el carácter con el que se dibujara")


print(f"cuadro de caracteres"  )
print ('--- Dibuja un cuadro de caracteres ---\n')

tamaño = int(input("¿De que tamaño sera el lado del Cuadro? "))
caracter = input("¿Que caracter quieres usar? ")

for fila in range(tamaño):
    for columna in range(tamaño):
        
        if fila == 0 or fila == tamaño - 1 or columna == 0 or columna == tamaño - 1:
            print(caracter, end=" ")
        else:
            
            print(" ", end=" ")
    
    print()







