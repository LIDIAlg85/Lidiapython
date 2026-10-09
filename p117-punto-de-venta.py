 # p117-punto-de-venta.py
 # Crear un sistema simple de punto de venta (POS) para un puesto de comida.

 # Crear un sistema simple de punto de venta (POS) para un puesto de comida.
comida = {
	 "Hamburguesa": 5.0,
	 "Papas Fritas": 2.5,
	 "Refresco": 1.5,
	 "Hot Dog": 3.0,
	 "Pizza": 8.0
 }

# Mostrar Menú: Mostrar al usuario los productos disponibles y sus precios, iterando sobre el diccionario
print("═" * 33, end="")
print("Menú de productos:")
for producto, precio in comida.items():
    print(f"- {producto}: ${precio:.2f}")

# Tomar Orden: Pedir al usuario que desea ordenar en un bucle.
# Si el producto no está en el menú, informarle.
# Si el producto existe, solicitar la cantidad.
orden = {}
while True:
    producto = input("Ingrese el producto que desea ordenar (o\npresione <Enter> para finalizar): ")
    if producto == "":
        break
    if producto not in comida:
        print("Producto no disponible. Intente nuevamente.")
        continue
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
    if producto in orden:
        orden[producto] += cantidad
    else:
        orden[producto] = cantidad

# Mostrar el ticket
print("Su orden:")
for producto, cantidad in orden.items():
    precio = comida[producto] * cantidad
    print(f"{producto}: {cantidad} x ${comida[producto]:.2f} = ${precio:.2f}")

total = sum(comida[producto] * cantidad for producto, cantidad in orden.items())
print(f"Total a pagar: ${total:.2f}")

