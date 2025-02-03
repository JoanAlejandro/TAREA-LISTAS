def repeticion(lista):
    # la funcion set elimina los duplicados de una lista
    if len(lista) != len(set(lista)):
        return True  # Si el tamaño de la lista es diferente al tamaño del conjunto, hay duplicados
    return False

l1 = [1, "Hola", 3, 4, "Hola"]
print(repeticion(l1))  
l2 = [1, 2, 3, 4, 5]
print(repeticion(l2))  
