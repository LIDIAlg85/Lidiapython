# p079-suma-potencias.py
# Suma las potencias de un número x desde x^1 hasta x^n

print("\033[H\033[J")
print("--- Suma de Potencias ---\n")

x = float(input("Numero base  x: "))
n = int(input("Cuantos términos (n): "))
suma_total = 0

print(f"\nCalculando la serie S = x^1 + ... + x^{n}")

for i in range(1, n + 1):
  termino_actual = 1
  for j in range(i):
     termino_actual *= x
  print(f"{x}^{i}" + (" + " if i < n else ""), end="")
  suma_total += termino_actual

print(f"\nResultado de la serie es: {suma_total}")