# p047-conteo-descendente-v2.py
# Imprime los números de n a 1, en intervalos  de m

print("\033[2J\033[H")
print("Imprime los números de n a 1, en intervalos  de m usando while")

n = int(input("Desde donde ? "))

c = n

while c >= 1:
  print(f" {c}", end="")
  c -= 1
print("\nProceso terminado", c)