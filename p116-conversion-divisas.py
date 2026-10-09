# 116-conversion-divisas.py
# Implementar un conversor de divisas a pesos mexicanos (MXN).
# Definir un diccionario de conversiones con las tasas de cambio.
# cambio (ej. 'USD', 'EUR', 'GBP', 'JPY', 'CAD') a MXN.
#
# borrar la consola
print("\033c", end="")
#
# Definir el diccionario de conversiones
conversiones = {
    "USD": 18.50, # 1 USD = 18.50 MXN
    "EUR": 20.00, # 1 EUR = 20.00 MXN
    "GBP": 23.00, # 1 GBP = 23.00 MXN
    "JPY": 0.14, # 1 JPY = 0.14 MXN
    "CAD": 14.00, # 1 CAD = 14.00 MXN
}

# Solicitar al usuario ingrese la cantidad y divisa de origen y valida divisa válida
cantidad = float(input("Ingrese la cantidad a convertir: "))

while True:
    divisa_origen = input("Ingrese la divisa de origen (USD, EUR, GBP, JPY, CAD): ").upper()
    if divisa_origen in conversiones:
        break
    print("Divisa no válida. Intente nuevamente.")

# Mostrar el resultado de la conversión a pesos mexicanos (MXN)
pesos_mxn = cantidad * conversiones[divisa_origen]
print("Resultado de la conversión:")
print(f"Cantidad {cantidad} {divisa_origen} = {pesos_mxn:.2f} pesos mexicanos (MXN).")
 