def palindromo(lista):
    return lista == lista[::-1]

lista1=['r','a','d','a','o']
if palindromo(lista1):
    print("La lista es palindrome")
else:
    print("La lista no es palindrome")