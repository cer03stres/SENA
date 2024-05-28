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
}0.

'''
#Composinión, contener 1 o mas instancias de otros objetos como si fueran atributos, meter clases dentro de otras clases
#Herencia, heredar varios atributos de otras clases
#Herencia multiple "                " muchas clases  

class Coche():
 #init metodo principal
 def __init__ (self):
   self.informacion = {}


 def obtener_info(self):
     self.informacion['marca'] = input("Ingrese la marca")
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

#Ejemplo de Composoción

class Motor:
  def __init__(self, tipo):
    self.tipo = tipo

  def arrancar(self):
    print("El modo de tipo", self.tipo, "ha arrancado")

class Automovil:
  def __init__(self, marca, modelo, motor):
    self.marca = marca
    self.modelo = modelo
    self.motor = motor

  def encender(self):
    print("Encendido el autómovil", self.marca, self.modelo)
    self.motor.arrancar()

motor_coche = Motor("Gasolina")
coche = Automovil("Toyota", "Corolla", motor_coche)
coche.encender()

#Ejemplo de Herencia Multiple
class Animal():
  def moverse(self):
    print("El animal se está moviendo")

class Volador():
  def volar(self):
    print("El animal está volando")

class Ave(Animal, Volador):
  def cantar(self):
    print("El ave está cantando")

#Instancia
ave = Ave()

#Invocando el método de la clase animal
ave.moverse()

#Accedemos al método de la clase Volador
ave.volar()

#Accedemos al método de la clase Ave
ave.cantar()

#Comentario