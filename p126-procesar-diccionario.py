#p126-procesar-diccionario.py
#● Define dos listas:o nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
#o sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]
#● Crea un diccionario nómina combinando ambas listas (los nombres son las llaves, los sueldos son los valores).
#● Muestra el diccionario nómina resultante.
#● Itera sobre el diccionario y muestra su contenido de cuatro formas:

#borrador de pantalla de consola 
print('\033[H\033[J')

#Crea un diccionario de nombres y sueldos
print('Nombres y Nomina:')

nombre_sueldos={
'Juan':4550.22, 'Pedro':8456.88, 'Manuel':1235.12, 'Elias':9998.00, 'Maria':12345.50, 'Felipe':29456.55, 'Julia':12234.00, 'Roberto':2000.00 
}
sueldos={

}
#diccionario  nombres y sueldos 
print('\nDiccionario  de Nómina:')
print(nombre_sueldos)

#Itera sobre el diccionario y muestra su contenido de cuatro formas:
#Mostrando solo las llaves (usando keys()).
print('\n---Interando llaves (keys)---:')
for llave in nombre_sueldos.keys():
	print(llave)
	
#Mostrando solo los valores (usando values()).
print('\n---Interando Valores (Values)---:')
for sueldo in nombre_sueldos.values():
	print(sueldo)

#Iterando por las llaves y accediendo al valor (ej. for llave in dic: ...).
print('\nIterando por las llaves y Valor:(accediendo por llave)')
for llave in nombre_sueldos:
	print(f'{llave}: {nombre_sueldos[llave]}')
	
#Mostrando la llave y el valor simultáneamente (usando items()).
print('\nInterando Llave y valor (items):')
for llave, sueldo in nombre_sueldos.items():
	print(f'{llave}: {sueldo}')

#Calcula y muestra la suma total de los sueldos.
print('\n---Calculos---:')
total_sueldos = sum(nombre_sueldos.values())
print(f'\nSuma total de los sueldos: {total_sueldos:.2f}')

#Calcula y muestra el promedio de los sueldos.
promedio_sueldos = total_sueldos / len(nombre_sueldos)
print(f'Promedio de los sueldos: {promedio_sueldos:.2f}')
