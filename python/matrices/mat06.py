#Crear juego 3 en raya

def crear_matriz(f,c):
    mat = []
    for i in range(f):
        mat.append(['_']*c)
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
    x = input("ubique    Fila: ")
    y = input("ubique Columna: ")
    data = raw_input("Ingrese Ficha: ")
    mat[x][y] = data
    
def evaluar_ganador(mat):
    for i in range(3):

        if mat[i] == ['x','x','x']:
            print "Ganastes"
	else:
	    print "sigue"

fila = 3
columna = 3


mat1 = crear_matriz(fila, columna)
reportar_matriz(mat1, fila)
std = 1

#print "Jugador 1:"
#ingresar_posicion(mat1)
#reportar_matriz(mat1,fila)

#print "Jugador 2"
#ingresar_posicion(mat1)
#reportar_matriz(mat1,fila)

while std !=0:
    
    ingresar_posicion(mat1)
    reportar_matriz(mat1,fila)
    evaluar_ganador(mat1)
    std = input("continuar? [1/0] :")

