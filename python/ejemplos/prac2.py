#programa que ingresa nombre, apellido1, apellido2
#luego imprime en pantalla el nombre completo

#entrada
nombres = raw_input("Ingrese Nombres: ")
ape_pat = raw_input("Ingrese Apellido Paterno: ")
ape_mat = raw_input("Ingrese Apellido Materno: ")
pro	= "Ing."
#proceso
nom_com = nombres + " " + ape_pat
#salida

print "%s%s " % (pro, nom_com)
