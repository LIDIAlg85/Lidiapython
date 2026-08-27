# p30-verifica-suma.py
# Verificar si la suma de dos números es igual a un tercero.
# 10 20 30    10 20 30    30 20 10

print("\033[2J\033[H")
print(' Verificar si la suma de dos números es igual a un tercero ')

print('Dame 3 números enteros separados por espacio')
n1, n2, n3 = map(int, input().split())


n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 + n2 == n3:
  print(f' n1 + n2 es igual a n3 ({n1} + {n2} = {n3})')
elif n1 + n3 == n2:
  print(f' n1 + n3 es igual a n2 ({n1} + {n3} = {n2})')
elif n2 + n3 == n1:
  print(f' n2 + n3 es igual a n1 ({n2} + {n3} = {n1})')
else:
  print('\nNo hay sumas')
  