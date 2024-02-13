class LenguajeProgramacion:
    def __init__(self, nombre, fecha_creacion, creadores, tipo,):
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.creadores = creadores
        self.tipo = tipo

    def crear_diccionario(self):
        return{
            'Nombre': self.nombre,
            'Fecha de creacion': self.fecha_creacion,
            'Creadores': self.creadores,
            'tipo': self.tipo,
        }
    
    def imprimir_informacion(self):
        info = self.crear_diccionario()
        for clave, valor in info.items():
            print(f"{clave}: {valor}")


        
        
nombre_lenguaje = input ("Ingrese el nombre del lenguaje de programacion ")
fecha_creacion = input ("Ingrese la fecha de creacion del lenguaje ")
creadores = input ("Ingrese el nombre de los creadores ")
tipo = input ("Ingrese el tipo de lenguaje ")

lenguaje = LenguajeProgramacion(nombre_lenguaje, fecha_creacion, creadores, tipo)

print ("La información es:" )

lenguaje = lenguaje.imprimir_informacion()

