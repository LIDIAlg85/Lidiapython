# p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones matemáticas para redondeo 
import math as mt

print("\033[2J\033[1;1H")


precio = 15.65

print(f"precio original  ${precio:.2f}")
print(f"arriba           ${mt.ceil(precio):.2f}")
print(f" abajo           ${mt.floor(precio):.2f}")
print(f"truncar          ${mt.trunc(precio):.2f}")
print(f" automatico      ${round(precio):.2f}")
print(f"automatico dec   ${round(precio, 1):.2f}")