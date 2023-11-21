'''
Algoritmo de calculadora en consola
con las operaaciones basicas.
'''
print ("CALCULADORA CON OPERACIONES BASICAS DE 2 NUMEROS")
print ("INGRESE LA OPCIÓN QUE DESEA REALIZAR")
print ("1 SUMA")
print ("2 RESTA")
print ("3 MULTIPLICACION")
print ("4 DIVISION")

opcion = int (input ("Seleccione una Opción"))


if opcion == 1:
 print ("Ha seleccionado la opción SUMA")
 numero1 = int (input("Ingrese el número 1"))
 numero2 = int (input("Ingrese el número 2"))
 resultado = numero1 + numero2
elif opcion == 2:
 print ("Ha seleccionado la opción RESTA")
 numero1 = int (input("Ingrese el número 1"))
 numero2 = int (input("Ingrese el número 2"))
 resultado = numero1 - numero2
elif opcion == 3:
 print ("Ha seleccionado la opción MULTIPLICACION")
 numero1 = int (input("Ingrese el número 1"))
 numero2 = int (input("Ingrese el número 2"))
 resultado = numero1 * numero2
elif opcion == 4:
 print ("Ha seleccionado la opción DIVISION")
 numero1 = int (input("Ingrese el número 1"))
 numero2 = int (input("Ingrese el número 2"))
 resultado = numero1 / numero2
else:
 print("Ha seleccionado una opción incorrecta")
print ("el resultado es:", resultado)