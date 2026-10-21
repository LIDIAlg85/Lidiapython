#p131-conjunto-numeros.py
#Operacion de numeros- conjuntos

print('\033[H\033[J')

#Dadas las siguientes tres listas de números:
print("---Conjuntos de Numeros--- ")
Lista1= ['50', '60', '70', '80', '90', '100', '200']
Lista2= ['60', '90', '100', '300', '400', '500']
Lista3= ['10', '20', '60', '90', '70','100','600','700']

#1. Crear y mostrar los conjuntos A, B y C a partir de las listas.
A = set(Lista1)
B = set(Lista2)
C = set(Lista3)

print('Conjunto A:', A)
print('Conjunto B:', B)
print('Conjunto C:', C)

#2. Calcular y mostrar los resultados de las siguientes operaciones:Unión (A | B) ,Unión (B | C), Diferencia (A - C),Diferencia Simétrica (B ^ C),Intersección (B & C)
# Operaciones de conjuntos
print('\n---Unión---')
print('Unión (A | B):', A | B)
print('Unión (B | C):', B | C)

print("\n--- Diferencia de conjuntos---")
print('Diferencia (A - C):', A - C)
print('Diferencia Simétrica (B ^ C):', B ^ C)
print('Intersección (B & C):', B & C)

#3. Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes preguntas:, ¿Es A subconjunto de B?,¿Es C subconjunto de A?,¿Está el número 100 en A?, ¿Está el número 60 en A, B y C?,¿No está el número 900 en C?
print("\n--- Subconjuntos---")
print('¿Es A subconjunto de B?:', A <= B)
print('¿Es C subconjunto de A?:', C <= A)
print('¿Está el número 100 en A?:', '100' in A)
print('¿Está el número 60 en A, B y C?:', all('60' in conjunto for conjunto in (A, B, C)))
print('¿No está el número 900 en C?:', '900' not in C)
