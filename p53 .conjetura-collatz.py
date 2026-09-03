# p53- conjetura-collatz.py
#Imprime la conjetura de collatz
#Dado n, si es par n/2, si es impar 3n+1, hasta llegar a n



while True:

    print("\033[2J\033[H")
    print("Imprime los numeros de la secuencia de collatz")
    n = int(input("Dame un numero entero positivo ? "))
    while n != 1:
        print(f" {n}")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(n)
    if input("Deseas continuar(s/n) ?").upper() =="n": break

print("\n terminamos de imprimir las tablas ")
