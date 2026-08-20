# p010-operaciones-matematicas. py
# Demuestra el uso de los diferentes operadores aritméticos 

print("/033[2J/033{1;1H")
print('-' * 50)
print('Calculadora de Operaciones Matematicas') 
print("=" * 50)

x = 200.34
y = 3.22

suma = x + y
resta =x - y
multi =x * y
divi = x / y
modu = x % y
pot = x ** y
dive = x // y

print('resultado de las operaciones realizadas\n')
print("=" * 50)
print("numeros:{x},{y}")
print(f"Suma: {suma:>10.2f}")
print(f"Resta:{resta:>10.2f}")
print(f"Mult: {multi:>10.2f}")
print(f"Divi: {divi:>10.2f}")
print(f"Módu: {modu:>10.2f}")
print(f"pot:  {pot:>10.2f}")
print(f"Dive: {dive:>10.2f}")
print("=" * 50)