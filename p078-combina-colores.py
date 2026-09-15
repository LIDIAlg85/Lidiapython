# p078-combina-colores.py
# Genera combinaciones de dos colores o palabras

print('\033[H\033[J')
print("Genera combinaciones de dos colores o palabras\n")

colores = input("Dame los colores separados por comas: ").strip().split(',')
print(f"\nColores base: {colores}")
print("--- Combinaciones Posibles ---")

for color1 in colores:
 for color2 in colores:
  if color1 != color2:
   print(f"- {color1} y {color2}")
