# p101-clasificar-temperaturas.py
# Clasificacion en temperaturas en grados centigrados: en Fria ,templado y caliente usando compresion de listas


print('\033[H\033[J')
print("\033[1;34m" + "Clasificar temperaturas" + "\033[0m\n")

temperaturas = [15,22,30,10,25,18,35]

# Se clasifica las temperaturas usando compresion de listas
clasificacion = [
                'Fría' if t < 20 else
                'Templada' if t <= 30 else
                'Caliente'
                 for t in temperaturas
]
print(f'Temperaturas: {temperaturas}')
print(f'Clasificación: {clasificacion}')