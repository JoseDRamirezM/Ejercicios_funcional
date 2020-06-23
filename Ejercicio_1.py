def ultimos_digitos(lista):
    if lista == []:
        return []
    return [str(lista[0]%10)] + ultimos_digitos(lista[1:])

def unir(lista):
    return int("".join(lista))

print(unir(ultimos_digitos([123,456,789])))
