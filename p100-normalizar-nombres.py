# p100-normalizar-nombres.py
# De una lista de nombres con espacios y mayusculas  se normalizan los nombres con minuscula y sin espacios al inicio y al final


print('\033[H\033[J')
print("\033[1;34m" + "Normalizar nombres" + "\033[0m\n")

nombres = [' JUAN ', 'Maria  ', '', ' PEDRO  Ana ', 'luis']

# Se normalizan los nombres usando compresion de listas
nombres_normalizados = [ nombre.strip().lower() for nombre in nombres ]

print (f'Nombres originales: {nombres}')
print(f'Nombres normalizados: {nombres_normalizados}')