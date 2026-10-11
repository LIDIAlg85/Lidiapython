#p104-procesar-notas.py
#Leer un número indeterminado de notas (calificaciones) entre 0 y 100, deteniéndose cuando el usuario introduzca un 0. 
# Validar que todas las notas introducidas estén dentro del rango [0,100].
#Calcular e imprimir:

print('\033[H\033[J')

notas = []
suma_notas = 0
cantidad_notas = 0
nota_maxima = -1
nota_minima = 101

# Validar que todas las notas introducidas estén dentro del rango [0,100].
while True:
    nota = float(input("Introduzca una nota (0 para terminar): "))

    if nota == 0:
        break

    if nota < 0 or nota > 100:
        print("La nota ingresada está fuera del rango [0, 100]. Intente nuevamente.")
        continue

    notas.append(nota)
    cantidad_notas += 1
    suma_notas += nota

    if nota > nota_maxima:
        nota_maxima = nota

    if nota < nota_minima:
        nota_minima = nota

if cantidad_notas == 0:
    print("No se ingresaron notas.")
else:
    promedio = suma_notas / cantidad_notas
    notas_menores_al_promedio = [n for n in notas if n < promedio]

#Calcular e imprimir:

    print("\n....Resultados....")
    print(f"Cantidad de notas introducidas: {cantidad_notas}")
    print(f"Lista de notas completa: {notas}")
    print(f"Suma de notas: {suma_notas}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota máxima: {nota_maxima}")
    print(f"Nota mínima: {nota_minima}")
    print(f"Cantidad de notas menores al promedio: {len(notas_menores_al_promedio)}")
    print(f"Notas menores al promedio: {notas_menores_al_promedio}")
