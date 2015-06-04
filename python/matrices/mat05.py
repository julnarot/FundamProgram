#Crear Una funcion que permita crear una matriz nula e n x m 

def crear_matriz(f,c):
    mat = []
    for i in range(fila):
        mat.append([0]*columna)
    return mat


def reportar_matriz(mat,f):   
    for i in range(f):
        print mat[i]


def ingresar_matriz(mat,f,c):
    for i in range(f):
        for j in range(c):
	    data = input("Ingrese Valor: ")
	    mat[i][j]=data

def ingresar_posicion(mat, x, y, data):
    mat[x][y] = data

fila = input("Ingrese Numero de Fila: ")
columna = input("Ingrese Numero de Columnas: ")

mat1 = crear_matriz(fila, columna)
reportar_matriz(mat1, fila)
ingresar_matriz(mat1, fila, columna)
reportar_matriz(mat1, fila)

x = input("Ingrese posicion X: ")
y = input("Ingrese Posicion y: ")

valor = raw_input("Ingrese Ficha: ")

ingresar_posicion(mat1, x, y, valor)

reportar_matriz(mat1,fila)
