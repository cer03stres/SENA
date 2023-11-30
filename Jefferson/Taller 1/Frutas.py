'''
Una comercializadora de frutas vende unicamente dos clases de frutas: peras y manzanas
Un kilo de pera tiene un valor de $1500 y el de manzana es de $2500
'''
#Definir precios
kilo_Apple = 2500
Kilo_Pear = 1500

#Menu de opciones de frutas

fruit = int(input(" 1.Apples  2.Pears "))


#Operacion de cada fruta
if fruit == 1:

  apples = float(input("Please select how many kilos of apples "))
 
  apples = apples * kilo_Apple
 
  print("The price you page is: ", apples)

  print("Thanks for your purchase")

if fruit == 2:

   Pears = float(input("Please select how many kilos of pears "))
 
   Pears = Pears * Kilo_Pear
 
   print("The price you page is: ", Pears)
 
   print("Thanks for your purchase")

#Mensaje de aviso
if fruit > 2 or fruit == 0: print("Please select the number in 1 or 2")




  
   




 
 