#p52- tabla -convercion.py
# Imprime una tabla de conversion de Peso a Dolar 

tc=16.80 # Establecemos en tipo de cambio actual

while True:
    print("\033[2J\033[H")
    print("Tabla de Conversion de Peso a Dolar")
    print(f"Tipo de cambio: {tc}")
    print("-" * 40)

while  true: # valida que los valores inicial y finalsean correctos
     inicial=intfloat(input(" Valor inicial del rango? "))
     final=intfloat(input(" Valor final del rango? "))
     if inicial < final and inicial>0:break
     else: print("Error: inicial debe ser menor a final")

c= Inicial
print ('\nPeso\t\tDolar')
print("-" * 30)
while c <= final:
    print(f" {c:<10.2f}{c/tc:>10.2f}")
    c += 1

    if input('\n Deseas continuar  (S/N) ?').upper() == 'SN': break
        
print("\n Terminamos  de imprimir las tablas ...")

