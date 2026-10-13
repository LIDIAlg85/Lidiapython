# p120-reporte-ventas.py
# Crear una lista de diccionarios para representar un reporte de ventas
# Cada compra registrada> nombre del cliente, producto, cantidad y precio
#Cada compra  debe ser  un diccionario almacenado en una lista de compras

compras = []

#borrar la pantalla de consola
print('\033[H\033[J')

print("\n--- Registro de  compras de la tienda  ---\n")
n = int(input("Número de compras a registrar: "))
for i in range(1, n + 1):
    print(f'\n------ Compra {i} ------')
    compra = {
        "nombre": input("Nombre Cliente: "),
        "producto": input("Nombre Producto: "),
        "cantidad": int(input("Cantidad: ")),
        "precio": float(input("Precio: "))
    }
    compras.append(compra)

#Mostrar los datos de cada  compra en lista
print(f'\n--- Todas las compras: {len(compras)} elementos')

#Consolidar las compras por cliente
#al final quiero saber total de productos y dinero gastado
clientes = {}  # Diccionario de diccionarios
for compra in compras:
    cliente = compra["nombre"]
    if cliente not in clientes:
        clientes[cliente] = {"cantidad": 0, "subtotal": 0.0}
    clientes[cliente]["cantidad"] += compra["cantidad"]
    clientes[cliente]["subtotal"] += compra["cantidad"] * compra["precio"]

#Mostrar el reporte consolidado por cliente
print('\n--- Reporte de consolidado por Cliente ---\n')
for cliente, datos in clientes.items():
    print(f"Cliente: {cliente}")
    print(f"Cantidad Total de Productos: {datos['cantidad']}")
    print(f"Total gastado: ${datos['subtotal']:.2f}\n")

print("\nDiccionarios de clientes con totales")
print(clientes)