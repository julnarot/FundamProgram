#Calcular la serie Fibonacci

m = input("Ingrese Limite: ")
a = 0
b = 1
while b < m:
    print b
    c = a + b
    a = b
    b = c
