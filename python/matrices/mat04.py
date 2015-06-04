# Suma de Matrices

x = input("Ingrese Fila: ")
y = input("Ingrese Columna: ")

matriz_a = []
matriz_b = []


for i in range(x):
    matriz_a.append([])
    for j in range(y):
        data = input("Ingrese Valor: [%d, %d]: " % (i,j)) 
	matriz_a[i].append(data)

for k in range(x):
    matriz_b.append([])
    for l in range(y):
        data = input("Ingrese Valor: [%d, %d]: "% (k,l))
	matriz_b[k].append(data)
print "MAtriz A: "
print matriz_a
print "Matriz B: "
print matriz_b

print "Suma de Matriz"
print matriz_a + matriz_b
