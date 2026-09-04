# p059-pares-descendente.py
## Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el usuario.

print('\033[H\033[J')
print("Imprimir los números pares y su suma total en un rango descendente desde 100 hasta n.")

n = int(input("Ingrese el número n: "))
pares = []
suma = 0
i = 100
while i >= n:
    if i % 2 == 0:
        pares += [i]
        suma += i
    i -= 1
print(f"Los números pares en el rango son: {pares}")
print(f"La suma total es: {suma}")

if input("\nDesea continuar  (S/N) ? ").upper()== "N":
   print("\n terminamos de imprimir los números pares ")