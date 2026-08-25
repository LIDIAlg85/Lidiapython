# p028-retira-cuenta.py
# Simula un retiro de dinero de una cuenta con validacion

saldo_cuenta =1500.00

print("\033[2J\033[H")
print("Simula un retiro de dinero de una cuenta con validacion \n")

cantidad_retiro = float(input(f"Cantidad a retirar de la cuenta saldo:(saldo_cuenta)? "))

if cantidad_retiro > 0:
   print('\nProcedemos al retiro ... ')
   if cantidad_retiro <= saldo_cuenta:
    nuevo_saldo = saldo_cuenta - cantidad_retiro
    print(f"\n Retiro exitoso, tu nuevo saldo es :{nuevo_saldo}")
   else:
    print(f'quieres retirar {cantidad_retiro} perotienes{saldo_cuenta}NO TE ALCANZA')
else:
    print("\n La cantidad a retirar debe ser un número positivo.")

print("\nGracias por usar nuestro servicio.")