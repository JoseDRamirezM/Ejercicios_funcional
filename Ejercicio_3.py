def tuplas(lista):
    if lista == []:
        return []
    return [(get_mayor(lista[0]), get_menor(lista[0]), 
            get_mayor(lista[0]) + get_menor(lista[0]))] + tuplas(lista[1:])

def get_mayor(lista):
    return max(lista)

def get_menor(lista):
    return min(lista)

print(tuplas([[1,3,5,10], [6, 2, 8, 9]]))