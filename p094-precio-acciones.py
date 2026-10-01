# p094-precio-acciones.py
# Analisis de precios de acciones diarias
#. Dada una lista de precios de cierre de una accion durante la semana
#Encontrar el preciomas alto, el mas bajo y el dia en que ocurrieron

print('\033[H\033[J')
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
precios = [150.25, 152.30,149.80,151.00, 153.45, 154.10, 155.00]

precio_alto = max(precios)
precio_bajo = min(precios)
dia_alto = dias[precios.index(precio_alto)]
dia_bajo = dias[precios.index(precio_bajo)]

print ('Analisis de precios de acciones:')
print(f'Precio más alto: {precio_alto} - Día: {dia_alto}')
print(f'Precio más bajo: {precio_bajo} - Día: {dia_bajo}')
