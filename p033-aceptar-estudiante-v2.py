# p033-aceptar-estudiante-v2.py
# Aceptar a un estudiante en base a la edad y calificaciones(usando AND )
#Las condiciones edad>=18 y c1 c2 >= 8

print("\033[2J\033[H")
print('Aceptar a un estudiante en base a la edad y calificaciones(usando AND )')

nombre = input('Dame tu nombre? ')
edad = int(input('Dame tu edad? '))

if edad >= 18: edad=20
 print(f'\n{nombre},  contintinuamos con el proceso..')
  print('Dame tus 2 calificaciones separadas por Enter ?')
  c1 = float(input())
  c2 = float(input())
  if c1 >= 8 and c2 >= 8: 
  print(f' {nombre} Bienvenido a la Universidad')
  else:
  print(f'\n {nombre}.no aceptamos calificaciones menores a 8 ..')
else:
  print(f'\n {nombre} no aceptamos menores de edad:.')    

print ('\n Proceso terminado')