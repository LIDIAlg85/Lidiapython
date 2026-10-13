# p118-lote-autos.py
# Crear una lista de diccionarios para almasenar  los datos de varios Autos 

autos = [
    {'marca': 'Toyota', 'modelo': 'Camary', 'año': 2020, 'precio': 25000},
    {'marca': 'Honda', 'modelo': 'Civic', 'año': 2019, 'precio': 22000},
    {'marca': 'Ford', 'modelo': 'Focus', 'año': 2021,'precio': 23000},
]
autos.append({'marca': 'Chebrolet', 'modelo': 'Malibu', 'año': 2022, 'precio': 27000})

#borrador de pantalla de consola 
print('\033[H\033[J')

#Mostrar los datos de cada Auto en la lista
print(f'\nTodos los autos : {autos}  {len(autos)} elementos')
print('\nDatos de cada auto:')
for auto in autos:
    print(auto)
    print()

#Mostrar los datos en forma de tabla
print('\nDatos en forma de Tabla:')
for k in autos[0].keys():
    print(f'{k}\t', end='')
print()
for auto in autos:
    for v in auto.values():
        print(f'{v}\t', end='')
    print()

#Mostrar los datos en forma de registro
print('\nDatos en forma de Registro')
for auto in autos:
    for k, v in auto.items():
        print(f'{k:<12} : {v}')
    print('')
