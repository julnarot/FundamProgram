#Crear juego 3 en raya

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
	    data = raw_input("Ingrese Valor: ")
	    mat[i][j]=data

def ingresar_posicion(mat):
    x = input("ubique columna: ")
    y = input("ubique fila: ")
    data = raw_input("Ingrese Ficha: ")
    mat[x][y] = data

fila = 3
columna = 3

estado = 10
while != 0:
    



mat1 = crear_matriz(fila, columna)
reportar_matriz(mat1, fila)
ingresar_matriz(mat1, fila, columna)
reportar_matriz(mat1, fila)
ingresar_posicion(mat1)
reportar_matriz(mat1,fila)
