# p145-cuadro-caracter
# Imprime un cuadro de caracteres

def cuadro_caracteres(caracteres:str, ancho: int, alto: int) -> None:
    """ Imprime un cuadro de caracteres"""
    for i in range(alto):
        for j in range(ancho):
            print(caracter, end='')
    print('') 

# Cuadro_caracteres(*', 10, 5)
caracter = input('Dame un carácter: ')
ancho = int(input('Dame el ancho: '))
alto = int(input('Dame el alto: '))
cuadro_caracteres(caracter, ancho, alto)

