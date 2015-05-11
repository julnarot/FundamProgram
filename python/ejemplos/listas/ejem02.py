# Ingrese un numero determinado de notas luego  calcule su promedio

tam = input("Ingres Numero de Notas: ")
notas = []
acum = 0
for i in range(tam):
    li = input("Ingrese Nota: ")
    notas.append(li)
    acum = acum + li
print acum / len(notas)
