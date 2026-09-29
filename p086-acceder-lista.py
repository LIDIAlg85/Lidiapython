## p086-acceder-lista.py
# Acceder a elementos de una lista

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]
print('\033[H\033[J')

print('Acceder a los elementos de una lista\n')
print('\nLongitud y contenido de las mediciones :')
print(f'Cuantas mediciones son : {len(nums)}')
print(f'Todas las mediciones : {nums} ')

print('\nPor indice positivo : ')
print(f'Elemnto en el indice 0 y 8 : {nums[0]} - {nums[8]}')

print('\nPor indice negativo : ')
print(f'Elemento en indice -9 y -1 : {nums[-9]}- {nums[-1]}')

print('\nPor rango : ')
print(f'De la 2 ala 6 (sin incluir el 6):') 
print('\nElementos :{nums[2:6]} ')

print ('\nPor Saltos:')
print(f'Elementos con saltos de 2 : {nums[::2]}')
print(f'Elementos con saltos de 3 : {nums[::3]}')