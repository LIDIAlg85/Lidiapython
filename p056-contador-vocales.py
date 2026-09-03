# p056-contador-vocales.py
# Dada una frase, cuenta vocales, consonantes y otros 


while True:
 print('\033[H\033[J')
 print("Dada una frase, cuenta vocales, consonantes y otros \n")

 frase = input("\nIntroduce una frase: ").lower()
 print(f"\nFrase a analizar es: {frase} y tiene {len(frase)} caracteres")

 i=vocal =consonante= otro = 0
 while i < len(frase):
  c= frase[i]
  print (c,end='')
  if 'a'<=c<='z':
   print ('si')
   if c in 'aeiou':
    vocal += 1
   else:
    consonante+= 1
 else:
    print('no')
    otros += 1
 i += 1
 print(f"vocales: {vocal}\n consonantes: {consonante} \notros: {otro}")