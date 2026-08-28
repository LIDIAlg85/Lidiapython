# p040-calculo-notas.py
# Escribe un programa que calcule el promedio de 5 calificaciones ingresadas por el usuario
# Menor a 6 reprobado,menos 7 pasas de panzazo,8 muy bien,9exelente,10 perfecto 

print("\033[2J\033[H")

nota1 = float(input("Ingrese la primera calificación: "))
nota2 = float(input("Ingrese la segunda calificación: "))
nota3 = float(input("Ingrese la tercera calificación: "))
nota4 = float(input("Ingrese la cuarta calificación: "))
nota5 = float(input("Ingrese la quinta calificación: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print(f"El promedio de las calificaciones es: {promedio}")

if promedio < 6:
    print("Quedas reprobado.")
elif promedio >= 6 and promedio >= 7:
    print("Pasas de panzazo.")
elif promedio >= 7 and promedio >= 8:
    print("Muy bien, puedes mejorar.")
elif promedio >= 8 and promedio >= 9:
    print("Excelente, sigue así.")
elif promedio >= 9 and promedio >= 10:
    print("Perfecto, tu esfuerzo valió la pena.")
else:
    print("Error: una o más calificaciones están fuera del rango permitido.")