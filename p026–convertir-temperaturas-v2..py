# p026–convertir-temperaturas-v2.py
# Convierte temperaturas de Celcius a Farenheit y viceversa

print("\033[2J\033[1;1H",end="")
print("Convierte temperaturas de Celcius a Farenheit y viceversa\n")
print('[1] Convertir de Farenheit a Celcius')
print('[2] Convertir de Celcius a Farenheit')
op = int (input("Elige ? "))

if op ==1:
print("\n🔜 Convirtiendo a Celcius...")
f = float(input("Introduce los grados Fahrenheit: "))
c = (f - 32) * 5 / 9
print('✅Los grados Celcius son: '+ str(f))

else:
    if op ==2:
print("\n🔜 Convirtiendo a Celcius...")
print("\n Convirtiendo de Celcius a  Fahrenheit")
c = float(input("Dame la temperatura en grados Celcius ? "))
f = (c * 9 / 5) + 32
print('✅Los grados Farenheit son : '+ str(f))

else:
print(f"\n Opción INVALIDA") 

print("\n Programa finalizado . .")