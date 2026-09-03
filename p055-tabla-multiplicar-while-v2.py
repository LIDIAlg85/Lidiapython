# p055-tabla-multiplicar-while-v2.py
# Imprime las tablas del 1 al 10, hasta el 10

while True:
    print("\033[2J\033[H")
    print("Imprime las tablas del 1 al 10, hasta el 10\n")

    n=int(input("Hasta cual tabla quieres ? "))
    m=int(input("Hasta donde llega. ? "))
  
    t = 1

    while t <= n:
        print(f" tabla del {t} \n")
        c = 1
        while c <= 10:
            print(f"{t:3} x {c:3} = {c*t}")
            c += 1

        t += 1

    if input("\nDesea continuar  (s/n) ? ").upper()== "n": break
    
print("\n terminamos de imprimir las tablas ")