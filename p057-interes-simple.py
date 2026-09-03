# p057-interes-simple.py
# Calcula los años necesarios para alcanzar una meta de ahorro

while True:
 print('\033[H\033[J')
 print("Calcula los años necesarios para alcanzar una meta de ahorro")

 ci= float(input("Capital inicial? "))
 ti= float(input("Tasa de interés anual (%)? "))
 ma= float(input("Meta de ahorro? "))

ca=ci
años=iaf=0
td=(ti/100)

while ca <= ma:
  print (f'{años}-{ca:,.2f}')
  iaf =ca*td
  ca+=iaf
  años+= 1

print (f'Para llegar a {ma:,.2f} deben pasar {años} años,el capital es {ca:,.2f}')

