class Animal():
    def hacer_sonido(self):
        pass
    def dormir (self):
        pass

class Leon(Animal):
    def hacer_sonido(self):
        print("El Leon Hace:")
        print("Roar")
    def dormir(self):
        print("El León está dormido")
        print("ZzZz")

           

    

class Tigre(Animal):
    def hacer_sonido(self):
        print("El Tigre Hace:")
        print("Rugido")
    def dormir(self):
        print("El Tigre está dormido")
        print("ZzZz")

        
    
def escuchar_sonidos_del_zoo(animales):
    for animal in animales:
        animal.hacer_sonido()
        animal.dormir()



leon = Leon()
tigre = Tigre()

escuchar_sonidos_del_zoo([leon,tigre])






