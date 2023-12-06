class Animal():
    def __init__ (self, nombre):
        self.nombre = ""

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return super().hacer_sonido()