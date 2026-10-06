# p103-resumen-ventas_v2.py
# Transforma una lista de ventas usando una funcion y comprension de listas
# La transformacion aplica 3 pasos en una misma funcion
# La funcion procesa la transformacion; luego, el programa principal la llama

# Esta funcion aplica una transformacion a cada elemento que recibe como parametro (una venta)
# Regresa el resultado de la transformacion
def transformar_venta(venta):
    # Paso 1: si la venta es mayor o igual a 1000, aplica un descuento del 10%
    if venta >= 1000:
        venta = venta * 0.9
    else:
        # Paso 2: si la venta es menor a 1000, aplica un descuento del 5%
        venta = venta * 0.95
    return venta


print("\033[2J\033[1;1H")
print("\033[1;34m" + "Resumen de ventas v2" + "\033[0m")

# Ventas del mes (10), algunas con decimales
ventas = [1000, 2000, 3000, 400, 500, 1500.50, 800.75, 1200.25, 600.60, 2500.80]
ventast = [transformar_venta(venta) for venta in ventas]

print("Ventas originales:", ventas)
print("Ventas transformadas:", ventast)
