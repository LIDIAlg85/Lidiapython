# p140-func-param-nombre.py
# Ejemplo de funcion con parametros con nombre 

def saluda(apaterno: str, amaterno: str, nombre: str) -> None:
   
   print(f'Hola {nombre} {apaterno} {amaterno}')

saluda('Castaneda ', 'Ramirez', 'Carlos')
saluda(nombre='Carlos', amaterno='Ramirez', apaterno='Castaneda')
#saluda(nombre ='Carlos')