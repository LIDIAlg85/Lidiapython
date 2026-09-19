#p080-compara-rendimiento-inversion.py
#Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años. 
# monto inicial y la tasa de interés anual (porcentaje) para cada uno de los dos fondos

print("\033[H\033[J")
print("Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años\n")

print( "---Fondo de inversión A---\n")
monto_inicial_1=float(input("Monto Inicial: "))
ti=float(input("Tasa de interés anual: "))
print(f"Tasa de interés para el Fondo A: {ti}%\n")

print( "---Fondo de inversión B---\n")
monto_inicial_2=float(input("Monto Inicial: "))
ta=float(input("Tasa de interés anual: "))
print(f"Tasa de interés para el Fondo B: {ta}%\n")

años=int(input(" Años a proyectar: "))
print("\n---Comparacion de Rendimientos Anuales--- \n")
print("\nAño\tFondo A\t\tFondo B")

for i in range(1, años + 1):
    monto_inicial_1 += monto_inicial_1 * (ti / 100)
    monto_inicial_2 += monto_inicial_2 * (ta / 100)
    print(f"{i}\t{monto_inicial_1:.2f}\t\t{monto_inicial_2:.2f}")
print("\n---Resultado Final--- \n")
if monto_inicial_1 > monto_inicial_2:
    print(f"El Fondo A generó un mayor rendimiento: {monto_inicial_1:.2f} > {monto_inicial_2:.2f}")
elif monto_inicial_2 > monto_inicial_1:
    print(f"El Fondo B generó un mayor rendimiento: {monto_inicial_2:.2f} > {monto_inicial_1:.2f}")





