# p095-registro-estudiantes.py
#Planteamiento del problema: Registro de estudiantes para evento
#• Se está organizando un evento y necesitas registrar a los asistentes.
#• El programa debe permitir al usuario introducir el nombre y la edad de cada
#persona.
#• El registro termina cuando se introduce un * como nombre.
#• Al finalizar, el sistema debe mostrar dos informes:
#• una lista de todos los asistentes que son mayores de edad (18 años o más).
#• y el nombre y la edad de la persona con mayor edad para entregarle un reconocimiento.

print('\033[H\033[J')
nombres = []
edades = []
while True:
    nombre = input("Ingrese el nombre del asistente (o '*' para terminar): ")
    if nombre == '*':
        break
    try:
        edad = int(input(f"Ingrese la edad de {nombre}: "))
        nombres.append(nombre)
        edades.append(edad)
    except ValueError:
        print("Edad inválida. Por favor, ingrese un número entero.")

# Filtrar asistentes mayores de edad
asistentes_mayores = [(nombres[i], edades[i]) for i in range(len(nombres)) if edades[i] >= 18]

# Encontrar la persona con mayor edad
persona_mayor = nombres[edades.index(max(edades))], max(edades)

# Mostrar informes
print('\033[H\033[J')
print('Informes del registro de asistentes\n')

print('Asistentes mayores de edad:')
for nombre, edad in asistentes_mayores:
    print(f'  - {nombre}: {edad} años')

print(f'\nPersona con mayor edad: {persona_mayor[0]} ({persona_mayor[1]} años)')
