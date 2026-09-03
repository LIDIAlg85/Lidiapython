# p054-tabla-multiplicar-while-v1.py
# Imprime la tabla de multiplicar del 1 al 10 usando while

print("\033[2J\033[H")

print("Imprime la tabla de multiplicar del 1 al 10 usando while\n")

t=int(input("Que tabla quieres ? "))
n= int(input("Hasta donde ? "))

print("\nImprimiendo la tabla del" +str (t))

c=1
while c<=n:
  print(f"{t:3} x {c:3} = {c*t}")
  c+=1






