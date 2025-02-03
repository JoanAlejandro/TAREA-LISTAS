def repe_vocal(cadena):
    i=sum(1 for c in cadena.lower() if c in "aeiou")
    if i>=2:
        return True    
    else:
        return False

lista=['Bebe','Luz','Csa']
j=0
for palabra in lista:
    if repe_vocal(palabra):
        print(palabra)
        j=j+1
if j==0:
    print("No existe")

