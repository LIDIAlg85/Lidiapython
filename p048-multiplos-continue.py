# p048-multiplos-continue.py
# Imprime solo los múltiplos de 10 de 1  a 200.

print("\033[2J\033[H")
print(" Imprime  múltiplos de 10 de 1 a 200")

c = 0
while c < 100:
  c += 1
  if c % 10 != 0: continue
  print(f"{c}", end=" ")

print("\n multiplos  terminados .")
