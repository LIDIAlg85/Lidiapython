#p125-eliminar-diccionario.py
#Crea un diccionario municipios con los datos: Apozol: 1863, Calera: 1868, Fresnillo: 1554, Guadalupe:
#1821, Jalpa: 1824, Jerez: 1824, Loreto: 1931, Mazapil: 1824, Momax: 1857.
#● Muestra el diccionario inicial.
#● Realiza las siguientes eliminaciones, mostrando el estado del diccionario después de cada operación:


#borrador de pantalla de consola 
print('\033[H\033[J')

#Crea un diccionario de municipios
print('MUNICIPIOS:')
municipios= {
'Apozol': 1863,
'Calera': 1868,
'Fresnillo': 1554,
'Guadalupe':1821,    
'Jalpa':1824,
'Jerez': 1824,
'Loreto': 1931, 
'Mazapil': 1824,
'Momax': 1857
}
#diccionario inicial
print('\nDiccionario Inicial:')
print(municipios)

#Realiza las siguientes eliminaciones
# (Elimina Apozol (usando del).)
del municipios['Apozol']
print("\nDespués de eliminar Apozol con la funcion (del):")
print(municipios)

#Elimina Fresnillo (usando pop()).
municipios.pop('Fresnillo')
print("\nDespués de eliminar Fresnillo con pop():")
print(municipios)

#Elimina el último elemento insertado (Momax) (usando popitem()).
municipios.popitem()
print("\n Después de popitem() eliminando Momax:")
print(municipios)

#Vacía el diccionario (usando clear()).
municipios.clear() 
print("\n Después clear():")
print(municipios)

#Muestra el diccionario final (vacío).
print("\nDiccionario final (vacío):")
print(municipios)
