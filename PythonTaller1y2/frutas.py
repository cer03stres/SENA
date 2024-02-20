print ("Seleccione una opción") 
print ("1 Pera")
print ("2 Manzana")
pera = 1500
manzana = 2500
opciones = int(input ("Ingrese la opción"))

if opciones == 1: 
 print ("Has seleccionado Pera")
 cantidadPeras = int(input ("Ingrese la Cantidad de Peras que va a comprar"))
 total_peras = pera*cantidadPeras
 print ("El valor a pagar de las peras es:", total_peras)
 print ("Gracias por su compra!! :)")
elif opciones == 2:
 print ("Has seleccionado Manzana")
 cantidadManzanas = int(input ("Ingrese la Cantidad de Manzanas que va a comprar"))
 total_manzanas = manzana*cantidadManzanas
 print ("El valor a pagar de las peras es:", total_manzanas)
 print ("Gracias por su compra!! :)")
else:
 print ("Ha seleccionado una opción incorrecta")
 
