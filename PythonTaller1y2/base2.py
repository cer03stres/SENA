
#Funcion que calcula el area de un triangulo, solicitando como argumentos la base y la altura

def resultadoArea(a,b):
 area=a*b/2
 return area


areaT = float(input("Ingrese el valor del area"))  
alturaT = float(input("Ingrese el valor de la altura"))  

area_resultante = resultadoArea(areaT,alturaT)
print ("El area es:", area_resultante)