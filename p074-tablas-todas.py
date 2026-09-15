 #p074-tablas-todas.py
 # Imprime las tablas de multiplicar de 1 a 10,de 1 al 10

print('\033[H\033[J')
print('Imprime las tablas de multiplicar de 1 a 10,de 1 al 10')

t = 3
n = 4

for i in range(1, n + 1):
    print('='*30)
    print(f" Tabla del {i} ")
    print('='*30)
    
    for j in range(1, n + 1):
       
        print(f"{i} x {j} = {i * j}")

    print('='*30)
    print()
print ("\nProceso terminado")        
