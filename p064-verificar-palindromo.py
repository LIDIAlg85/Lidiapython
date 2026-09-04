# p064-verificar-palindromo.py
## Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).

print('\033[H\033[J')
print("Verificar si un número es palíndromo.")

numero = int(input("Ingrese un número entero: "))
numero_str = str(numero)

if numero_str == numero_str[::-1]:
    print(f"El número {numero} es un palíndromo.")
else:
    print(f"El número {numero} no es un palíndromo.")

if input("\nDesea continuar  (S/N) ? ").upper()== "N" "S":
    print("\nProceso terminado")
