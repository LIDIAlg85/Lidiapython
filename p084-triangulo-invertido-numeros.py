#p084-triangulo-invertido-numeros.py
#Un número entero n que determinará la altura de un triángulo numérico invertido.

print("\033[H\033[J")
print("Un número entero n que determinará la altura de un triángulo numérico invertido")

n = int(input("Dame un numero: "))

for i in range(n, 0, -1):
    for renglon in range(1, i + 1):
        print(renglon, end=" ")
        
    print()  
