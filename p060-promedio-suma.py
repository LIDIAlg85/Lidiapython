# p060-promedio-suma.py 
## Leer números introducidos  hasta que ingrese un 0, mostrar el conteo total de números, la suma y el promedio de la serie.

print('\033[H\033[J')
print("introduce numeros (0 para terminar)")

conteo = 0
suma = 0
while True:
    n = int( input(" > "))
    if n == 0:
        break
    conteo += 1
    suma += n

if conteo > 0:
    promedio = suma / conteo
    print(f"Conteo total de números: {conteo}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron números.")

if input("\nDesea continuar  (S/N) ? ").upper()== "N":
   print("\n Terminamos de Imprimir los Números  ")  