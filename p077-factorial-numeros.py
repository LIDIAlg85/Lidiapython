#p077-factorial-numeros.py
# Calcula el factorial de n números  

print('\033[H\033[J')
print("Calcula el factorial de n números\n")
    
try:
   n = int(input("¿Hasta el número ? "))

   for x in range(1, n + 1):
      print(f"({x})! ", end="")
      factorial = 1

      for i in range(1, x + 1):
         factorial *= i
      print(f"{i}{'x' if i > 1 else ''} = {factorial:,}")

except :
   print("Introduce un número entero válido.")