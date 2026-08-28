# p036-numeros-consecutivos.py
# Escribe un programa que reciba tres números enteros y determine si son consecutivos.

print("\033[2J\033[H")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 + 1 == num2 and num2 + 1 == num3:
    print("Los números son consecutivos.")
else:
    print("Los números no son consecutivos.")







