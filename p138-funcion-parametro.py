# p138-funcion-parametro.py
# Ejemplo de una funcion con parametros

def saluda(nombre: str) -> None:
   print(f'Hola {nombre} bienvenido a Python, tu nombre tiene {len(nombre)} caracteres')

saluda('Carlos Castaneda')
saluda('Juan Perez Diaz')
saluda('María Soto García')
saluda('Carlos Antonio')