# p093-consolidar-ventas.py
# una empresas tiene 2 sursales y desea consolidar cada una de ellas
# Se ingresa n ventas de cada sucursal  y  el usuario lo define


ventas_1 = []
ventas_2 = []
ventas_consolidada = []

print('\033[H\033[J')
print('Consolidación de ventas de dos sucursales\n')

n = int(input('Ingrese el número de ventas para cada sucursal: '))

for i in range(n):
    venta_1 = float(input(f'Ingrese la venta {i+1} de la sucursal 1: '))
    ventas_1.append(venta_1)
    venta_2 = float(input(f'Ingrese la venta {i+1} de la sucursal 2: '))
    ventas_2.append(venta_2)

# Consolidar las ventas
ventas_consolidada = ventas_1 + ventas_2

# Calcular totales
total_1 = sum(ventas_1)
total_2 = sum(ventas_2)
total_consolidado = sum(ventas_consolidada)

# Mostrar resultados
print('\033[H\033[J')
print('Resultados de la consolidación de ventas\n')
print(f'Total de ventas sucursal 1: {total_1}')
print(f'Total de ventas sucursal 2: {total_2}')
print(f'Total consolidado: {total_consolidado}')

