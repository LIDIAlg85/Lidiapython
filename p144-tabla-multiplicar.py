# p144-tabla-multiplicar.py
# Una funcion que imprime la tabla de multiplicar de un numero hasta n


def tabla_multiplicar(tabla: int, hasta: int) -> None:
    """Imprime la tabla de multiplicar de un número hasta el límite indicado."""
    print(f'Tabla de multiplicar del {tabla} hasta {hasta}:')
    for i in range(1, hasta + 1):
        print(f'{tabla} x {i} = {tabla * i}')

#tabla_multiplicar(3, 12)
tabla = int(input('Tabla de multiplicar: '))
hasta = int(input('¿Hasta dónde quieres llegar?: '))
tabla_multiplicar(tabla, hasta)

