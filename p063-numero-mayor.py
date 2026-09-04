# p063-numero-mayor.py
##Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, el programa deberá mostrar cuál fue el número más grande de todos los introducidos.

print('\033[H\033[J')
print("Ingrese números (0 para terminar)")

numero = float(input("> "))
numero_mayor = numero

while numero != 0:
    numero = float(input("> "))
    if numero > numero_mayor:
        numero_mayor = numero

print(f"El número mayor fue: {round(numero_mayor)}")

if input("\nDesea continuar  (S/N) ? ").upper()== "N":
   print("\nProceso terminado")