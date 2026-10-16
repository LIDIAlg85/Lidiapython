# p123-modificar-diccionario.py
# Crea un diccionario llamado paises con los siguientes pares (llave: valor): Argentina: 100, Brasil: 200,Colombia: 300, Chile: 400, Ecuador: 500, Bolivia: 600, Jamaica: 700.
# ● Muestra el diccionario inicial.
# ● Modifica los valores de las siguientes llaves:

#borrador de pantalla de consola 
print('\033[H\033[J')

#Crea un diccionario llamado paises con los siguientes pares (llave: valor)
print('Diccionario llamado paises:')
paises= {
   'Argentina': 100,
   'Brasil': 200,
   'Colombia': 300,
   'Chile': 400,
   'Ecuador': 500,
   'Bolivia': 600,
   'Jamaica': 700
}
#diccionario inicial
print('\nDiccionario Inicial:')
print(paises)

#Valores Modificados de las siguientes llaves
paises['Brasil'] = 250
paises['Chile'] = 450
paises.update({'Bolivia': 650})
paises.update({'Jamaica': 750})

#diccionario modificado
print('\nDiccionario Modificado :')
print(paises)
