# p061-suma-200.py
## Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200, mostrando los números introducidos y la suma final.
 
print('\033[H\033[J')
print("Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200, mostrando los números introducidos y la suma final")

suma = 0
numeros_introducidos = []
cantidad_numeros = 0

while suma < 200:
      numero = float(input("Introduce un número: "))
      numeros_introducidos += [numero]
      cantidad_numeros += 1
      suma += numero

if suma >= 200:
    print(f"meta alcanzada: {suma >= 200}")
    print(f"Suma final: {suma}")
    print(f"Total de números introducidos: {cantidad_numeros}")

if input("\nDesea continuar  (S/N) ? ").upper()== "N":

 print("\nProceso terminado")







