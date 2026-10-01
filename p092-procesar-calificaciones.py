# p092-procesar-calificaciones.py
# Procesa calificaciones entre 0 y 10, calcula el promedio y muestra la calificación más alta y más baja.
# al final, muestra un resumen de las calificaciones ingresadas.
# cuantos alumnos aprobaron (calificación >= 6) y cuántos reprobaron (calificación < 6).
# valida que no introduscan letras en  lugar de numeros  

print('\033[H\033[J')
print('Procesador de calificaciones de un curso\n')
print("Introduce calificaciones entre 0 y 10 (usa 99 para terminar):\n")
calificaciones = []
suma = 0.0
aprobaron = 0

while True:
    try:
        calificacion = float(input("Calificación: "))
        if calificacion == 999:
            break
        elif calificacion < 0 or calificacion > 10:
            print("Calificación inválida. Debe estar entre 0 y 10.")
            continue
        else:
            calificaciones.append(calificacion)
            suma += calificacion
            if calificacion >= 6:
                aprobaron += 1
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número.")

if not calificaciones:
    print("No se ingresaron calificaciones.")
else:
    promedio = suma / len(calificaciones)
    print(f"\nResumen de calificaciones:")
    print(f"Promedio: {promedio:.2f}")
    print(f"Calificación más alta: {max(calificaciones)}")
    print(f"Calificación más baja: {min(calificaciones)}")
    print(f"Alumnos aprobados: {aprobaron}")
    print(f"Alumnos reprobados: {len(calificaciones) - aprobaron}")