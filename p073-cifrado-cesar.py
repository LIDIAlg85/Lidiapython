# p073-cifrado-cesar.py
# Cifra un mensaje con desplaamientos  (Cifrado César).


print('\033[H\033[J')
print(' Cifrado de César')

mensaje_original = input(" Mensaje : ")


desplazamiento = int(input(" Desplazamiento ? "))

mensaje_cifrado = ""

for caracter in mensaje_original:
        if caracter.isalpha() and caracter.isascii():
            codigo_ascii = ord(caracter)
            base = ord('a') if caracter.islower() else ord('A')
            codigo_nuevo = base + (codigo_ascii - base + desplazamiento) % 26
            mensaje_cifrado += chr(codigo_nuevo)
        else:
            mensaje_cifrado += caracter

print(f"\nMensaje cifrado: {mensaje_cifrado}")
print(f"Mensaje original: {mensaje_original}")

input("\nPresiona Enter para continuar...")
    
