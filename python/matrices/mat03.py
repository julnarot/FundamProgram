# Indicar si es una Matriz es Rectangular

x = input("Ingrese Fila: ")
y = input("Ingrese Columna: ")

matriz = []
suma = 0
for i in range(x):
    matriz.append([])
    for j in range(y):
        data = input("Ingrese Valor: [%d], [%d]:" % (i,j)) 
	matriz[i].append(data)

print matriz
