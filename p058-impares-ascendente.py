# p058-impares-ascendente.py
## Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el usuario.

print('\033[H\033[J')
print("Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta n.")

n = int(input("Ingrese el número n: "))
impares = []
suma = 0
i = 1
while i <= n:
    if i % 2 != 0:
        impares += [i]
        suma += i
    i += 1
print(f"Los números impares en el rango son: {impares}")
       
print(f"La suma total es: {suma}")

if input("\nDesea continuar  (S/N) ? ").upper()== "N":  
   
   print("\n terminamos de imprimir los números impares ") 
   
   






