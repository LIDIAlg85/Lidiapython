#p142-func-mas-param.py
#Funcion que recibe n parametros y los Imprime en pantalla

def saluda(*nombres: str) -> None:
   print(nombres)
   for nombre in nombres:
    print(f"Hola  {nombre} bienvenido a python, tu nombre tiene {len(nombre)} caracteres")

def edades(edades : list[int]) -> None:
   print(edades)
   for edad in edades:
    print(f"edad es: {edad} años")

saluda("Carlos Castaneda","Juan","Pedro")
edades([25, 30, 35])