#Su script debe solicitar al usuario digitar la cantidad de calificaciones que desea ingresar y de las que calculará un 
#promedio final. El script deberá pedir cada una de las calificaciones, finalmente deberá imprimir el promedio final.
 
calificaciones = int(input("Ingrese la cantidad de Estudiantes: "))
 
lista = []
posicion = 1
totalIngresadas = calificaciones
 
while calificaciones > 0:
    valor = float(input("Ingrese calificación {}: ".format(posicion)))
    lista.append(valor)
    calificaciones -= 1
    posicion += 1
 
print(lista)
 
sumaNotas = 0
for i in lista:
    sumaNotas = sumaNotas + i
 
promedio = round(sumaNotas/totalIngresadas,2)
 
print("El promedio de las notas ingresadas es: {}".format(promedio))