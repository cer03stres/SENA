# manzanas_y_peras
print ("Seleccione una opción")
print ("1. Peras")
print ("2. Manzanas")
peras = 1500
manzanas = 2500
opciones = int(input ("Ingrese la opción"))
if opciones == 1:
 print("A seleccionado peras")
 cantidad = int(input ("Ingrese la cantidad de peras que desea"))
 total_peras = cantidad * peras
 print("El valor a pagar es:", total_peras)
 print("¡Gracias por su compra!")
elif opciones == 2:
 print("A seleccionado manzanas")
 cantidad = int(input ("Ingrese la cantidad de manzanas que desea"))
 total_manzanas = cantidad * manzanas
 print("El valor a pagar es:", total_manzanas)
 print("¡Gracias por su compra!")
else:
 print("Opción no válida")