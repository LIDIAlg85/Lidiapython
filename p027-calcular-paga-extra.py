# p027-calcular-paga-extra.py
# Calcula la paga de un trabajador considerando horas extra.

print("\033[2J\033[H")
print('Calculando la paga de un trabajador considerando horas extra ')


print("Dame tus datos")
nombre = input('Nombre : ')
horas = int(input('Horas : '))
paga_hora = float(input('Paga x hora: 

horas_extra = paga_extra = 0

if horas > 40:
    pagar_normal =40 * pagar_hora
    horas_extra = horas - 40
    paga_extra = horas_extra * (paga_hora * 2)

else:
     paga_normal=horas *paga_hora

total =paga_normal + paga_extra

print(" Cálculo de pagos ")
print(f'El trabajador {nombre} trabajo {horas} horas a una paga de  {paga_hora}') 
print(f'El pago normal  : ${paga_normal}')
print(f'Horas extra     : ${Horas extra}')
print(f' Paga extra     : ${paga_extra}')
print(f'TOTAL.          :{TOTAL}')

print('\n Proceso terminado...')