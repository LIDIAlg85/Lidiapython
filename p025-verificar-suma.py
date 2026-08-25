# p025-verificar-suma.py
# Dados los tres numeros enteros, verifica si la suma es igual al tercero
#10+20 ==30(son iguales ) 5+8==5 (son diferentes)

print("\033[2J\033[1;1H",end="")
print('Dados los tres numeros enteros, verifica si la suma de los dos primeros es igual al tercero\n' )

n1 = int(input('Dame el primer número  1 ? '))
n2 = int(input('Dame el segundo número 2 ? '))
n3 = int(input('Dame el tercer número  3 ? '))



if  n1 + n2 == n3:
  print(f'✅{n1 }+{n2+}={n3}SON IGUALES')
else:
  print(f'❌{n1 }+{n2+}!={n3} SON DIFERENTES')

print('\nFin del programa.')