# Encuentre el mayor y el menor valor de una lista

tam = input("Ingrese Tamanio de la Lista: ")
lista = []
mayor = 0
menor = 999
for i in range(tam):
    data = input("Ingrese Numero: ")
    lista.append(data)

for i in range(tam):
    if lista[i] > mayor:
        mayor = lista[i]
    
    if lista[i] < menor:
        menor = lista[i]

print lista
print mayor
print menor


