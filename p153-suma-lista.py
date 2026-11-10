#p153-suma-lista.py
# Función para sumar los elementos de una lista


def suma_lista(lista: list[float]) -> float:
   '''Suma los elementos de una lista de numeros.'''
   suma = 0.0
   for numero in lista:
      suma += numero
   ## lista^[0]=0 no se recomienda modificar la lista original   
   return suma

# Programa principal
numeros = [1.5, 2.3, 3.7, 4.1, 10.22]
resultado = suma_lista(numeros)
print(f"La suma de de los elementos de la lista({numeros}) es: {resultado}")


