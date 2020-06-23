class Nodo():
	def __init__(self, valor, izquierda=None, derecha=None):
		self.valor = valor
		self.izquierda = izquierda
		self.derecha = derecha

def en_orden(arbol):
	if(arbol==None):
		return []
	return en_orden(arbol.izquierda) + [arbol.valor] + en_orden(arbol.derecha)

def separar(num):
    return [int(x) for x in str(num)]

def digitos_arbol(lista):
    if lista == []:
        return []
    return [separar(lista[0])] + digitos_arbol(lista[1:])

#Arbol binario ordenado
 
print(digitos_arbol(en_orden(Nodo(25,Nodo(15,None,Nodo(20)),Nodo(50)))))