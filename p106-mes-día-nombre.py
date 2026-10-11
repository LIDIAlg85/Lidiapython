#p106-mes-día-nombre.py
#Leer un número de mes (ej. 4). Guardar los días de cada mes en una lista y los nombres de los meses en otralista. 
#Asumir 28 días para febrero. Imprimir el nombre del mes y la cantidad de días del mes correspondiente (ej.marzo, 30).

print('\033[H\033[J')
# Guardar los días de cada mes en una lista y los nombres de los meses en otra
dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nombres_de_los_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Leer un número de mes
mes = int(input("Introduzca el número de mes (1-12): "))

# Validar el número de mes
if 1 <= mes <= 12:
    # Imprimir el nombre del mes y la cantidad de días
    print("\n--- Resultados ---")
    print(f"Mes: {nombres_de_los_meses[mes - 1]}") 
    print(f"Días: {dias_del_mes[mes - 1]}")