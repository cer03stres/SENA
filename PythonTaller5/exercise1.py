class Calculadora():
 def suma(self, num1, num2):
  return num1 + num2
 def resta(self, num1, num2):
  return num1 - num2
 def multiplicacion(self, num1, num2):
  return num1 * num2
 def division(self, num1, num2):
    if num2 == 0:
     print("No se puede dividir un numero entre 0")
    else:
     return num1/num2
#Se llama a la clase calculadora

def Principal():
 #Instancia de la clase Calculadora
 calculadora = Calculadora()
 
 print ("CALCULADORA DE OPERACIONES DE 2 NUMEROS")
 print ("seleccione una opción")
 print ("1 Suma")
 print ("2 Resta")
 print ("3 Multiplicación")
 print ("4 División")
 print ("5 Salir")
 opciones = int(input("Ingrese una opción " )) 

 while opciones > 5:
  print ("Opción incorrecta") 
  print ("CALCULADORA DE OPERACIONES DE 2 NUMEROS")
  print ("seleccione una opción")
  print ("1 Suma")
  print ("2 Resta")
  print ("3 Multiplicación")
  print ("4 División")
  print ("5 Salir")
  opciones = int(input("Ingrese una opción " )) 


 if opciones == 1:
  print("Has elegido Suma")
  num1 = float(input("Ingrese el primer número " ) )
  num2 = float(input("Ingrese el segundo número ") )
  print("Resultado Suma:", calculadora.suma(num1, num2))    

 if opciones == 2:
  print("Has elegido Resta")
  num1 = float(input("Ingrese el primer número " ) )
  num2 = float(input("Ingrese el segundo número ") )
  print("Resultado Resta:", calculadora.resta(num1, num2))    

 if opciones == 3:
  print("Has elegido Multiplicación")
  num1 = float(input("Ingrese el primer número " ) )
  num2 = float(input("Ingrese el segundo número"  ) )
  print("Resultado Multiplicación:", calculadora.multiplicacion(num1, num2))    

 if opciones == 4:
  print("Has elegido División")
  num1 = float(input("Ingrese el primer número " ) )
  num2 = float(input("Ingrese el segundo número" ) )
  print("Resultado División:", calculadora.division(num1, num2))    

 if opciones == 5:
  print("Cerrando calculadora")
  


#Llamado a clase main
Principal()