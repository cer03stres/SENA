'''
Desarrollar un algoritmo que calcule el area de un triangulo
dada su base y altura
'''
def calcular_area (base, altura):

 area = (base*altura)/2
 return area

#Solicitar la base y la altura del triangulo para calcular el area 

base_triang = float(input("Ingrese el valor de la base"))
altura_triang = float(input("Ingrese el valor de la altura"))
area_resultante = calcular_area(base_triang, altura_triang)

print ("El area del triangulo con base: ", base_triang, " y altura: ", altura_triang, " Es: ", area_resultante)
