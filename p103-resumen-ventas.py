# p103-resumen-ventas.py
# Transforma y filtra ventas con comprensiones

print('\033[H\033[J')
print("\033[1;34m" + "Resumen de ventas" + "\033[0m\n")

ventas = [1000,2000,3000,400,500]# Ventas del mes

#Ventas mayores a 1000 se les aplica un descuento del 10% , menores a 1000 se aplica el 5% de descuento
ventas_descuento = [v * 0.9 if v > 1000 else v * 0.95 for v in ventas]

#saques ventas relevanter si son mayores a 500
Ventas_relevantes = [v for v in ventas_descuento if v > 500]

print(f'Ventas originales: {ventas}')
print(f'Ventas finales: {ventas_descuento}')
print(f'Ventas mayores de $500: {Ventas_relevantes}')
print(f'Total relevante: ${sum(Ventas_relevantes):.2f}')