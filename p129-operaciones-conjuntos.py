#p129-operaciones-conjuntos.py
#Operaciones con conjuntos

c1 = {1, 2, 3, 4, 5}
c2 = {5, 6, 7, 8, 9, 10}
c3 = {9, 10, 11, 12, 13}
c4 = {3, 4, 5}

print('\033[H\033[J')

print("Conjuntos Base ")
print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"c3: {c3}")
print(f"c4: {c4}")

#Union de conjuntos
print("\nUnion de conjuntos")
print(f"c1 union c2: {c1.union(c2)}")
print(f"c1 union c3: {c1 | c3}")

#Interseccion de conjuntos
print("\n--- Intersección de conjuntos ---")
print(f"c1 intersección c2: {c1.intersection(c2)}")
print(f"c2 intersección c3: {c2 & c3}")

#Diferencia de conjuntos
print("--- Diferencia de conjuntos---")
print(f"c1 - c2: {c1.difference(c2)}")
print(f"c2 - c3: {c2 - c3}")

# Diferencia sistemiva de conjuntos
print("\n--- Diferencia Simétrica de conjuntos---")
print(f"c1 dif c2: {c1.symmetric_difference(c2)}")
print(f"c2 dif c3: {c2 ^ c3}")

# Subconjuntos y superconjuntos
print("\n--- Subconjuntos y Superconjuntos ---")
print(f"¿c4 es subconjunto de c1? : {c4.issubset(c1)}")
print(f"¿c3 es subconjunto de c2? : {c3.issuperset (c2)}")

#Superconjuntos
print("\n--- Superconjuntos ---")
print(f"¿c1 es superconjunto de c4? : {c1.issuperset(c4)}")
print(f"¿c2 es superconjunto de c3? : {c2 >= (c3)}")

#Pertenencias y no pertenencias
print("\n--- Pertenencia y no pertenencia---")
print(f"5 pertenencia c1? : {5 in c1} ")
print(f"6 No pertenenciaestá a c1? : {6 not in c1}")