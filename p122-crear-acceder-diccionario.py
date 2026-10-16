# p122-acceder-diccionario.py
# Crea un diccionario llamado dias usando llaves numéricas para los días de la semana.
# ● Muestra el diccionario completo.
# ● Accede y muestra los siguientes valores específicos:

#borrador de pantalla de consola 
print('\033[H\033[J')

#Diccionario llamado dias  usando llaves
print('Crea un Diccionario llamado dias')
dias = {
    1: 'Lunes',
    2: 'Martes',
    3: 'Miércoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sábado',
    7: 'Domingo'
}

# Diccionario completo
print('\nDiccionario completo:')
print(dias)

# Acceso a valores específicos
print('\nValor de la llave 1 usando []:', dias[1])
print('Valor de la llave 7 usando []:', dias[7])
print('Valor de la llave 5 usando get():', dias.get(5))
print('Valor de la llave 7 usando get():', dias.get(7))

#Vuelve a mostrar el diccionario completo
print('\nDiccionario completo:')
print(dias)
