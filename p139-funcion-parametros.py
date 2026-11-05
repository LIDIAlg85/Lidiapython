# p139-funcion-parametros.py
#Ejemplo de funcion con varios parametros


def saluda(apaterno: str, nombre: str) -> None:
   print(f'Hola {nombre} {apaterno}')

saluda('Castaneda', 'Carlos')
# saluda('Carlos Castaneda') 
# saluda('Castaneda', 'Ramirez', 'Carlos') 