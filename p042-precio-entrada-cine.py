# p042-precio-entrada-cine.py
#Crear un programa para la taquilla de un cine que determine el precio de una entrada según la edad del cliente
## Solicitar edad y precio ,menores de 5 años es gratis,niños (5-12 años) pagan $5, adultos (13-64 años) pagan $10, tercera edad (65 y mas) pagan $7

print("\033[2J\033[H")
print("Determine el precio de una entrada según la edad del cliente")

edad = int(input("Ingrese su edad: "))

if edad < 5:
    precio = 0
elif 5 <= edad <= 12:
    precio = 5
elif 13 <= edad <= 64:
    precio = 10
   
else:
    precio = 7

print(f"El precio de la entrada es: ${precio}")