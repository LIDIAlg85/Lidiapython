# p089-eliminar-lista.py
# Eliminar elementos de una lista

print('\033[H\033[J')
print('Eliminar elementos de una lista')

nums = [1, 3, 5, 7, 9, 11,  15, 17, 19]

print('\nLongitud y contenido de la lista de numeros:')
print(f'Contenido: {nums} longitud:{len(nums)}')

print('\nEliminar el 15 de la lista')
nums.remove(15)
print(f'Contenido actualizado : {nums}longitud:{len(nums)} ')

print('\nEliminar el elemento en la posición 3')
del nums[3]
print(f'Contenido actualizado : {nums}longitud:{len(nums)} ')

print('\nEliminar el elemento en la posición 5 usando pop()')
num= nums.pop(5)
print(f'Contenido actualizado : {nums}longitud:{len(nums)} ')
print(f'Elemento eliminado: {num}')

print('\nEliminar el último elemento usando pop() sin parámetros')
num = nums.pop()
print(f'Contenido actualizado : {nums}longitud:{len(nums)} ')
print(f'Elemento eliminado: {num}')

print('\nEliminar todos los elementos usando clear()')
nums.clear()
print(f'Contenido actualizado: {nums} longitud:{len(nums)}')

