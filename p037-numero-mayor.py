# p037-numero-mayor.py
# Escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor

print("\033[2J\033[H")
print("Escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es: {num2}")
else:
    print(f"El número mayor es: {num3}")