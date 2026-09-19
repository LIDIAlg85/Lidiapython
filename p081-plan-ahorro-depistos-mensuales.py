#p081-plan-ahorro-depistos-mensuales.py
#Desarrolla un programa que ayude a un usuario a planificar su ahorro mensual para alcanzar una meta de ahorro.

print("\033[H\033[J")
print("Desarrolla un programa que ayude a un usuario a planificar su ahorro mensual para alcanzar una meta de ahorro.\n")

meta_ahorro=float(input("Monto inicial de ahorro: "))
ahorro_mensual=float(input("Depósito mensual: "))
tasa_de_interes=float(input("Tasa de interés mensual (%): "))
numero_de_meses=int(input("Número de meses a simular: "))

saldo = meta_ahorro
deposito_mensual = ahorro_mensual
tasa_interes = tasa_de_interes / 100

print ("\n---Plan de Ahorro Detallado--- \n")
for mes in range(1, numero_de_meses + 1):
    interes = saldo * tasa_interes
    saldo_final = saldo + interes + deposito_mensual
    print(f"Mes {mes}: Saldo Inicial: ${saldo:.2f} | Interés: ${interes:.2f} | Saldo Final: ${saldo_final:.2f}")
    saldo = saldo_final

print(f"Al final de {numero_de_meses} meses, tendrás ${saldo:.2f}")



