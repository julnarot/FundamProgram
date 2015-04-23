#CALCULAR SI UN NUMERO ES PAR O IMPAR
#ENTRADA
n = input("Ingrese Numero: ")
mens = "estado"
#PROCESO
if n%2 == 0:
    mens = "El numero es PAR"
else:
    mens = "El numero es IMPAR"

#SALIDA
print mens
