# p032-aceptar-estudiante.py
# Aceptar a un estudiante en base a la edad y calificaciones(usando OR )
#Las condiciones edad>=18 y c1 c2 >= 8

print("\033[2J\033[H")
print('Aceptar a un estudiante en base a la edad y calificaciones(usando OR )')

nombre = input('Dame tu nombre? ')
edad = int(input('Dame tu edad? '))


if edad < 18:
  print(f'\n {nombre}. no aceptamos menores de edad..')
else:
  print(f'\n {nombre} continuamos con el proseso..')
  print('Dame tus 2 calificaciones separadas por Enter ?')
  c1 = float(input())
  c2 = float(input())
  if c1 < 8 or c2 < 8: 
    print(f'\n {nombre}.no aceptamos calificaciones menores a 8:.')
  else:
    print(f' {nombre} Bienvenido a la Universidad')

print ('\n Proceso terminado')