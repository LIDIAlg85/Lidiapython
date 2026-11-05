# p141-func-param-defecto.py
#Uso de paarmetros  con valoes por defecto 

def calcular_total(monto: float, iva: float = 0.16) -> float:
   return monto + (monto * iva)

print(f"El total a pagar es: ${calcular_total(1000):,.2f}")
print(f"Total 2: ${calcular_total(1000, 0.10):,.2f}")