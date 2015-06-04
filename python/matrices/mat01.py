# Crear un Programa que permitar Crear una matriz de N x M
x = input("Ingrese Cantidad de Filas: ")
y = input("Ingrese Cantudad de Columnas: ")

matriz = []

for i in range(x):
    matriz.append([])
    for j in range(y):
        valor = input("Ingrese Valor: [%d,%d ]: " % (i,j))
	matriz[i].append(valor)
    
for i in range(len(matriz)):
    print matriz[i]


