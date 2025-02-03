def palindromo(cadena):
    # Comprobamos si la cadena es igual a su reverso
    return cadena == cadena[::-1]
j=0
lista=['hola','aloh','holdoh']
for palabra in lista:
    if palindromo(palabra):
        print(palabra)
        j=j+1
if j==0:
    print("No existe")
