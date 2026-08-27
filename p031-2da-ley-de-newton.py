# p031-2da-ley-de-newton.py
# Calculadora los valores de la 2da Ley de Newton

print("\033[2J\033[H")
print('--- Calculadora de la 2da Ley de Newton ---')
print('[F] Calcular la Fuerza (f = m * a)')
print('[M] Calcular la Masa (m = f / a)')
print('[A] Calcular la Aceleración (a = f / m)')
print('Elige?')
op = input().upper()

f = m = a  = 8
        
if op=='F':
  print('\n Calculando la Fuerza')
  m = float(input('Dame la masa? '))
  a = float(input('Dame la aceleración? '))
  fuerza = m * a 
  print('\nLa fuerza es' + str(f))
elif op == 'M':
  print('\n Calculando la Masa')
  f = float(input('Dame la fuerza? '))
  a = float(input('Dame la aceleración? '))
  m = f / a
  print('\n La masa es: ' + str(m))
elif op == 'A':
  print('\n Calculando la Aceleración')
  f = float(input('Dame la fuerza? '))
  m = float(input('Dame la masa? '))
  a = f / m
  print('\n La aceleración es: ' + str(a))
else:
    print('\n Opción incorrecta') 

print ('\n Proceso terminado')    