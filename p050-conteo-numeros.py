# p050-conteo-numeros.py
# El usuario introduce n numeros para con  999, se suma y se cuenta

print("\033[2J\033[H")
print('El usuario introduce n numeros para con  999, se suma y se cuenta')

c = suma = cp=cn=cz = 0

while True:
  num = int(input(' Número ? '))
  if num == 999: break
  c += 1 #contando
  suma+=num #acumulado
  if num > 0:
    cp+= 1 #contado
  elif num< 0:
    cn+= 1 #contado
  else:
    cz+=1 #contado

print("\nResumen de los calculos")
print(f'\nCuantos :(c)')
print(f'\nSuma    :(7)')
print(f'\nPos     :(cp)')
print(f'\nNeg     :(cn)')
print(f'\nZer     :(cz)')

print("\nProceso terminado")