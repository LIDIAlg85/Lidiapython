# p049-sumar-consecutivos.py
# Suma números hasta que el total sea >= 100.

print("\033[2J\033[H")
print("Suma números hasta que el total sea >= 100.")

c = 0
s = 0

while c < 200:
  c += 1
  s += c
  print(f" {c}")
  if s >= 100: break


print(f"La suma de  {s} despues de {c}numeros")