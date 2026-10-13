# p121-area-figuras.py
# Calculadora dinámica de áreas usando un diccionario de diccionarios

import math

figuras = {
    "1": {
        "nombre": "Círculo",
        "parametros": ["radio"],
        "formula": "pi * radio ** 2"
    },
    "2": {
        "nombre": "Triángulo",
        "parametros": ["base", "altura"],
        "formula": "base * altura / 2"
    },
    "3": {
        "nombre": "Rectángulo",
        "parametros": ["base", "altura"],
        "formula": "base * altura"
    }
}


def pedir_valores(figura):
    valores = {}
    for parametro in figura["parametros"]:
        while True:
            try:
                valor = float(input(f"{parametro.capitalize()} : "))
                valores[parametro] = valor
                break
            except ValueError:
                print("Valor inválido. Intenta de nuevo.")
    return valores


print('\033[H\033[J')
print('Área de Figuras Geométricas\n')
print("Calculadora de áreas de figuras geométricas")
print("Figuras disponibles:")
for clave, valor in figuras.items():
    print(f'{clave:<10} - {valor["nombre"]}: {valor["formula"]}')

while True:
    opcion = input('\nElige una figura (1, 2, 3): ').strip()
    if opcion in figuras:
        figura = figuras[opcion]
        break
    print("Error: Figura no válida. Intenta de nuevo.")

variables = {"pi": math.pi, **pedir_valores(figura)}
area = eval(figura["formula"], {"__builtins__": {}}, variables)
print(f"\nEl área del {figura['nombre']} es: {area:.4f}")