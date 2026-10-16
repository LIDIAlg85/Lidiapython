# p124-agregar-diccionario.py
# Crea un diccionario llamado ventas con los siguientes datos: Juan: 1550, Jose: 2600, Maria: 2220.
# Muestra el diccionario.
# Agrega los siguientes vendedores y sus ventas al diccionario:

#borrador de pantalla de consola 
print('\033[H\033[J')

# Crea un diccionario llamado ventas 
print('diccionario  Ventas')
ventas={
'Juan':1550,
'Jose':2600,
'Maria':2220
}
# diccionario de ventas 
print('\n Ventas Iniciales')
print(ventas)

#vendedores agregados + ventas
ventas['Rocio']=2500,
ventas['Mateo']= 1567,
ventas.update({'Andrea': 9567}),
ventas.update({'Miguel':1234})

#diccionario actualizado
print('\nVentas  Actualizadas')
print(ventas)