# p043-calculadora-anio-bisiesto.py 
# Escribe un programa que determine si un año, ingresado por el usuario es  bisiesto o no.   
## Un  año es bisiesto si es divisible entre 4, pero no entre 100, a menos que también sea divisible entre 400. 

print("\033[2J\033[H")
print("Determine si un año, ingresado por el usuario es bisiesto o no.")

año = int(input("Ingrese un año: "))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")

