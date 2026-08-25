# p029-calculadora-descuentos.py
# Simula una calculadora de descuentos basada en el monto de la compra

print("\033[2J\033[H")
print("Simula una calculadora de descuentos basada en el monto de la compra \n")

compra = float(input(" Total de tu compra: ?"))
descuento = porcentaje = 0

if compra > 2000:
    porcentaje = 0.20 
elif compra>2000
    porcentaje =0.10
elif compra>500:
    porcentaje= 0,05

descuento = compra * porcentaje
total = compra - descuento

print("\n--- Resumen de la Compra ---")
print(f"Total de la compra     : {compra:,.2f}")
print(f"Porcentaje de descuento: {int(porcentaje * 100)}%")
print(f"Ahorro por descuento   : {descuento:,.2f}")
print(f"Total a pagar          : {total:,.2f}")

print("\n¡Gracias por tu compra!")