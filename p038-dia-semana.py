# p038-dia-semana.py
# Solicite un número entero del 1 al 7 y muestre el día de la semana correspondiente considerando que 1 es domingo y 7 es sábado. 
#Si el número ingresado no es correspondiente ,  mostrar un mensaje de error.

print("\033[2J\033[H")
num = int(input("Ingrese un número del 1 al 7: "))

if num == 1:
    print("El día de la semana es domingo.")
elif num == 2:
    print("El día de la semana es lunes.")
elif num == 3:
    print("El día de la semana es martes.")
elif num == 4:
    print("El día de la semana es miércoles.")
elif num == 5:
    print("El día de la semana es jueves.")
elif num == 6:
    print("El día de la semana es viernes.")
elif num == 7:
    print("El día de la semana es sábado.")
else:
    print("Error: el número ingresado está fuera del rango permitido.")