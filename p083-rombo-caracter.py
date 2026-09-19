#p083-rombo-caracter.py
#Solicitar al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo.

print("\033[H\033[J")
print("Solicitar al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo")

print(f"Rombo de caracteres"  )
print ('--- Dibuja un Rombo de caracteres ---\n')

tamaño = int(input("Dame un numero impar para la Altura: "))
caracter = input("¿Que caracter quieres usar? ")
print()


for i in range(1, tamaño + 1, 2):
    espacios = (tamaño - i) // 2
    for espacios in range(espacios):
        print(" ", end="")
    for caracter in range(i):
        print(caracter, end="")

    print()

for i in range(tamaño - 2, 0, -2):
    espacios = (tamaño - i) // 2
    for espacios in range(espacios):
        print(" ", end="")
    for caracter in range(i):
        print(caracter, end="")
        
    print()  

