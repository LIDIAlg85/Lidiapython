# p035-tipo-triangulo.py
# Clasificar un triangulo segun la longitud de sus lados.

print("\033[2J\033[H")
print("--- CLASIFICADOR DE TRIANGULOS ---")
print("Clasificar un triangulo segun la lomgitus de sus lados.")

lado_a = float(input(" longitud de lado a: "))
lado_b = float(input(" longitud de lado b: "))
lado_c = float(input(" longitud de lado c: "))

if lado_a == lado_b and lado_b == lado_c:
  print(f" Es un triangulo EQUILATERO (todos los lados son iguales).")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
  print(f" Es un triangulo ISOSCELES (al menos dos lados son iguales).")
else:
  print(f" Es un triangulo ESCALENO (ningun lado es igual).")
  