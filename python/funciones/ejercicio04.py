# Funcion que Devuelve el valor menor de una lista


def crear_lista(tam):
    lis = []
    for i in range(tam):
        valor = input("Ingrese Valor: ")
	lis.append(valor)
    return lis

def buscar_menor(lis):
    menor = lis[0]
    for i in range(len(lis)):
        if menor >= lis[i]:
	    menor = lis[i]
    return menor


def ver_lista(lis):
    for i in range(len(lista)):
        print lis[i]

tamanio = input("Ingrese Tamanio de Lista: ")
lista = crear_lista(tamanio)
ver_lista(lista)
print "Valor Menor: ", buscar_menor(lista)



