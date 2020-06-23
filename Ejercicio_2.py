def lista_de_listas(lista):
    if lista == []:
        return []
    return [separar(lista[0])] + lista_de_listas(lista[1:])

def separar(num):
    return [int(x) for x in str(num)]

def multiplicar(lista):
    if lista == []:
        return []
    return [[(x * 3) for x in lista[0]]] + multiplicar(lista[1:])
    

print(multiplicar(lista_de_listas([234,563,342,781])))