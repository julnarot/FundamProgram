#Buscar datos de una Lista (Lineal)
tam = input("Ingrese Tamanio de Lista: ")
lista = []
for i in range(tam):
    data = input("Ingrese Valor: ")
    lista.append(data)

for i in range(tam):
    print lista[i]

menor = lista[0]

for i in range(tam):
    if menor >= lista[i]:
        menor = lista[i]
print "menor-> " , menor
