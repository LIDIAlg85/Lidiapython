# p062-conversion-temperaturas.py
## Conversión de temperaturas de Celsius a Fahrenheit en un rango especificado

print('\033[H\033[J')
print("Conversión de temperaturas de Celsius a Fahrenheit en un rango especificado.")

temp_inicial = float(input("Introduce la temperatura inicial en °C: "))
temp_final = float(input("Introduce la temperatura final en  °C: "))

if temp_inicial > temp_final:
    print("La temperatura inicial debe ser menor o igual a la temperatura final.")
    temp_inicial, temp_final = temp_final, temp_inicial

temp_celsius = int(temp_inicial)
while temp_celsius <= int(temp_final):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f"{temp_celsius}°C = {temp_fahrenheit}°F")
    temp_celsius += 1

if input("\nDesea continuar  (S/N) ? ").upper()== "N":
    print("\nProceso terminado")
