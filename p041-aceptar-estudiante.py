# p041-aceptar-estudiante.py
# Escribe un programa que determine si un estudiante es aceptado en una universidad basado en
#  nombre(?) genero (mujer), edad (mayor de 21 años) y  mostrar tres calificaciones  que den un promedio (8 a 9.5).

print("\033[2J\033[H")
print("Escribe un programa que determine si un estudiante es aceptado" )

nombre=input("Ingrese su nombre: ")     
genero = input("Ingrese su género (H/M): ").upper()
edad = int(input("Ingrese su edad: "))
cal1 = float(input("Ingrese su primera calificación: "))
cal2 = float(input("Ingrese su segunda calificación: "))
cal3 = float(input("Ingrese su tercera calificación: "))

promedio = (cal1 + cal2 + cal3) / 3

if nombre != "" and genero == "M" and edad > 21 and 9.5 >= promedio >= 8:
    print("Estudiante  si aceptado.")
else:
    print("Estudiante no aceptado por no cumplir con los requisitos.")

    
    