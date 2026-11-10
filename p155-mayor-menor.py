# p155-mayor-menor.py
# Se crean 2 funciones, una para encontrar el mayor y otra para encontrar el menor de una lista de números. 
# Se crea una función para capturar datos del usuario  y regresa una lista de numeros
	
def captura_numeros()-> list[float]:
    '''Captura números del usuario  y regresa una lista de números.'''
    numeros = []
    while True:
        entrada = input("Ingresa un número (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return numeros

def mayor(listas: list[float]) -> float:
    '''Regresa  el número mayor en la lista.'''
    if not listas:
        return None
    maximo = listas[0]
    for numero in listas:
        if numero > maximo:
            maximo = numero
    return maximo

def menor(listas: list[float]) -> float:
    '''Regresa  el número menor en la lista.'''
    if not listas:
        return None
    minimo = listas[0]
    for numero in listas:
        if numero < minimo:
            minimo = numero
    return minimo

# Programa principal
numeros = captura_numeros()
if not numeros:
    print("No se ingresaron números.")
else:
    print(f"Los numeros capturados son:{numeros}")
    elmasgrande = mayor(numeros)
    print(f"El mayor numero de lista es :{elmasgrande}")
    elmaspequeño = menor(numeros)
    print(f"El número menor es: {elmaspequeño}")

    