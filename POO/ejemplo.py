#Ejemplo de abstraccióm
"""
Abstracción
Simplificar cosas complejas mediante 
la creación de modelos.
Una clase es un modelo que define la estructura
y el comportamiento de los objetos.
"""
#Creación de clase Class

#def __init__ inicializa el constructor.
#Self habla del mismo objeto, el propio, lo llama.
#El constructor define los atributos de las clases.
class Coche():
 #Constructor (__init__) que se llama al crear un nuevo objeto
 def __init__(self, color, velocidad):
  self.color = "Rojo"
  self.velocidad = int


#Metodo para acelerar el coche

 def acelerar (self):
  #Incrementamos la velocidad
  self.velocidad += 10

  print("Acelerando. Nueva velocidad: ", self.velocidad)

#Metodo para frenar el  coche
 def frenar (self):
  #Disminuye la velocidad
  self.velocidad -= 5
  print("Frenando. Nueva velocidad: ", self.velocidad)

#Crear objetos de la clase coche



#Utilizar los metodos de los objetos
coche_rojo = Coche(color = "Rojo", velocidad = 0)
coche_azul = Coche(color = "Azul", velocidad = 0)
coche_rojo.acelerar()
coche_azul.frenar()