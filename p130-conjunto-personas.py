#p130-conjunto-personas.py
#Conjuntos de personas

print('\033[H\033[J')

#Dadas las siguientes dos listas de nombres:
print('\n---Personas---')
lista1 = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista2 = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

#1. Crear y mostrar los conjuntos A (basado en la Lista 1) y B (basado en la Lista 2).
print('\n---Lista 1 y 2---')
A = set(lista1)
B = set(lista2)

print("Conjunto A:", A)
print("Conjunto B:", B)

#2. Calcular y mostrar los resultados de las siguientes operaciones:Unión (A | B) , Intersección (A & B) ,Diferencia (A - B) , Diferencia Simétrica (A ^ B)
print('\n---Union---')
print("Unión (A | B):", A | B)
print("Intersección (A & B):", A & B)
print("Diferencia (A - B):", A - B)
print("Diferencia simétrica (A ^ B):", A ^ B)

#. Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes afirmaciones:, ¿Es {Pablo, Mateo} un subconjunto de B?
#o ¿Es A un superconjunto de {Reynaldo, Angelica}?, ¿Está "Pedro" en el conjunto A? ,¿No está "Lilia" en el conjunto B?
print('\n---Subconjuntos---')
print("¿{Pablo, Mateo} es subconjunto de B?", {"Pablo", "Mateo"}.issubset(B))
print("¿A es superconjunto de {Reynaldo, Angelica}?", A.issuperset({"Reynaldo", "Angelica"}))
print('¿"Pedro" está en A?', "Pedro" in A)
print('¿"Lilia" no está en B?', "Lilia" not in B)
