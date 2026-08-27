# p034-tipo-angulo.py
# Dado un angulo en el rango de 0 a 360 indicar que tipo de angulo es

print("\033[2J\033[H")
print('Dado un angulo en el rango de 0 a 360 indicar que tipo de angulo es')

ang = int(input(' ángulo : '))

if ang >= 0 and ang <= 360:
  print(f' Tu ángulo es de {ang} grados y es un ángulo ', end='')
  if ang < 90:
    print('AGUDO')
  elif ang == 90:
    print('RECTO')
  elif ang > 90 and ang < 180:
    print('OBTUSO')
  elif ang == 180:
    print('LLANO')
  elif ang > 180 and ang < 360:
    print('CÓNCAVO')
  elif ang == 360:
    print('CERRADO ')
else:
  print('\nEl ángulo está fuera del rango .')

print('\nproceso terminado ')  