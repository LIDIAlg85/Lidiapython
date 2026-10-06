# p102-aplanar-matriz.py
# Aplana una matriz de dos dimenciones a una lista de 1 dimencion usando comprecion de listas


print('\033[H\033[J')
print("\033[1;34m" + "Aplanar matriz" + "\033[0m\n")

matriz = [[1, 2, 3], [-4, 5, 6], [-7, 8, 9]]

# se Aplanan  la matriz usando compresion de listas
Aplanada  = [elemento  for fila in matriz for elemento in fila]
positivos = [elemento  for elemento in Aplanada if elemento > 0]
Negativos = [elemento  for elemento in Aplanada if elemento < 0]          


print(f'Matriz Original: {matriz}')
print(f'Lista Aplana: {Aplanada }')
print(f'elemento positivos: {positivos}')
print(f'elemento Negativos: {Negativos}')