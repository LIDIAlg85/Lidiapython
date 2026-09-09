# p071-suma-promedio-numeros.py
# Suma de n numeros introducidos por el usuario usando ciclo for


print('\033[H\033[J')
print('Suma de calificaciones introducidas por el usuario usando ciclo for')
n= int(input('Cuantas calificaciones ? '))

suma = 0
cadnum = ""

for i in range(1, n+1):
  calificacion = int(input(f'Calificación[{i}] = '))
  suma += calificacion
  cadnum = cadnum + ' ' + str(calificacion)
print(f'Calificaciones: {cadnum}')
print(f'La suma es {suma}, el promedio es {suma / n}')

if input('\n\nDeseas continuar (S/N) ? ').upper()=='N':
 print('\nHemos llegado al final ....')
