'''
Conceptos POO

POO > Paradigma de programación
programación orientada a objetos

Clase: Es la plantilla que me permite instanciar objetos

buenas practicas definir las clases con Mayuscula

Atributo: son las caractereisticas o propiedades de un objeto
ej: Color, tamaño, peso, edad

def Lucas():
 raza = "Pitbull"
 edad = 2
 peso = "10kg"
 vacuna = True

def Candy():
 raza = "schnauzer"
 edad  = 2
 peso  = "5kg"
 vacuna = False

Objeto: Entidad que posée caracteristicas llamadas
atributos y tiene acciones llamadas métodos.
un perro tiene atributos como nombre, edad, etc
y tiene métodos como ladrar y correr.

Metodo: Son acciones que un objeto puede
tomar.

Encapsulamiento: agrupar los datos y metodos en 1 sola unidad.
herencia: capacidad que tiene una clase de heredar atributos de otra clase.

Polimorfismo:

ejemplo encapsulamiento.

Class Perro{
#Atributos
 raza
 color
#Metodos
 Ladrar = "Guau"
 correr...
}

'''



class Coche():
 #init metodo principal
 def __init__ (self):
   self.informacion = {}


 def obtener_info(self):
     self.informacion['marca'] = input("In grese la marca")
     self.informacion['modelo'] = input("Ingrese el modelo")

 def imprimir_datos(self):
   print("Información del coche")
   print("Nombre de la Marca:",  self.informacion['marca'])
   print("Modelo:", self.informacion['modelo'])

 def imprimir_diccionario(self):
    return self.informacion

#Creacion de objetos

coche = Coche()

imprimir_diccionario = coche.imprimir_diccionario()

coche.obtener_info()
coche.imprimir_datos()

print("La información del coche es:",  imprimir_diccionario)

#Pas es para que no mande nada todavia