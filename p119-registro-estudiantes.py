# p119-registro-estudiantes.py
# Crear una lista de diccionarios para  almacenar los datos de varios estudiantes
#nombre ,edad, carrera, y promedio 

estudiantes  = [
    {'nombre': 'Juan Perez', 'edad': 20, 'carrera': 'Ingenieria en Sistemas', 'promedio': 8.5},
    {'nombre': 'Maria Lopez', 'edad': 22, 'carrera': 'Medicina', 'promedio': 9.2},
    {'nombre': 'Carlos Garcia', 'edad': 21, 'carrera': 'Arquitectura', 'promedio': 8.7}
]
#borrador de pantalla de consola
print('\033[H\033[J')

# Mostrar los datos de cada estudiante en la lista 
print(f"\nTodos los  estudiantes :- {estudiantes} - {len(estudiantes)} elementos")

#Captura de datos de un nuevo estudiante , hasta nombre vacio
while True:
    nombre= input('Ingrese el nombre del estudiante (o precione Enter  para salir): ')

    if nombre != '':
        break
    
    edad = int(input('Ingrese la edad del estudiante: '))
    carrera = input('Ingrese la carrera del estudiante: ')
    promedio = float(input('Ingrese el promedio del estudiante: '))
    estudiantes.append({'nombre': nombre, 'edad': edad, 'carrera': carrera, 'promedio': promedio})
    print(f"\nEstudiante {nombre} agregado correctamente.")

print(f'\nTodos los Estudiantes: {estudiantes}- {len(estudiantes)} elementos')

#Mostrar los datos en forma de tabla
print('\nDatos  de Estudiante en forma de Tabla:')
for k in estudiantes[0].keys():
    print(f'{k:<15}', end='')
print('')
for alumno in estudiantes:
    for v in alumno.values():
        print(f'{v:<15}', end='')
    print('')

# Mostrar los datos en forma de registro
print('\nDatos en forma de Registro y Cálculo de Promedios:')
for est in estudiantes:
    s += est['promedio']
    for k, v in est.items():
        print(f'{k:} : {v}')
    print('')

#Calcular  la suma y el promedio de los promedios de los estudiantes
suma_promedios = sum(est['promedio'] for est in estudiantes)
promedio = suma_promedios / len(estudiantes) if estudiantes else 0
print(f'\nSuma de los promedios : {s}')
print(f'Promedio General de los estudiantes es {promedio:.2f}')
