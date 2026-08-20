# p009-promedio-de-calificaciones
# Calcular el promedio de tres calificaciones ingresadas por el usuario

print("/033[2J/033{1;1H")
print('Calculando el promedio de tres calificaciones:\n')

# Entrada
print('Dame 3 calificaciones separadas por espacio')
cal1, cal2, cal3 = input().split()
cal1, cal2, cal3 = int(cal1), int(cal2), int(cal3)

# Proceso
suma=cal1 + cal2 + cal3
promedio = suma / 3

#salida
print(f'Las calificaciones son: {cal1}, {cal2}, {cal3}')
print(f'La suma es:{suma}, y el promedio es {promedio}')