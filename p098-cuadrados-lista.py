# p098-cuadrados-lista.py
# Genera cuadrados usando una comprensión de listas

#borrar  la pantalla  
print('\033[H\033[J')
print("\033[1;35m" + "Cuadrados de 1 a n usando compresión de listas" + "\033[0m\n")
n = int(input('ingrese el valor de n '))

numeros = list(range(1, n + 1))
cuadrados = [x** 2 for x in numeros]  # comprensión de listas para generar los cuadrados de los números del 1 al n

print(f"\033[1;35mNúmeros del 1 al {n} son:\033[0m \033[1;31m{numeros}\033[0m")
print(f"\033[1;35mLos cuadrados del 1 al {n} son:\033[0m \033[1;31m{cuadrados}\033[0m")