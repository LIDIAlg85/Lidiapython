# p146-numero-mayor
# Dados tres números enteros, regresar el mayor

def numero_mayor(n1: int, n2: int, n3: int) -> int:
    """ Devuelve el numero mayor de tres numeros """
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


print('Dame tres numeros enteros separados por <enter>')
n1, n2, n3 = int(input()), int(input()), int(input())
print(f'El numero mayor es: {numero_mayor(n1, n2, n3)}')
