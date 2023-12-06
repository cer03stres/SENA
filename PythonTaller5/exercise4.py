class LenguajeProgramacion:
    def __init__(self):
        self.datos = {}

    def ingresar_datos(self):
        self.datos['Nombre_Lenguaje'] = input("Ingrese el nombre del lenguaje de programación: ")
        self.datos['fecha_creacion'] = input("Ingrese la fecha de creación del lenguaje: ")
        self.datos['creadores'] = input("Ingrese el nombre o nombres de los creadores")
    def imprimir_info(self):
        print("\nInformación del lenguaje de programación:")
        print("Nombre:", self.datos['Nombre_Lenguaje'])
        print("Fecha de Creación:", self.datos['fecha_creacion'])
        print("Creadores:", self.datos['creadores'])

    def imprimir_diccionario(self):
        return self.datos

# Crear una instancia de la clase LenguajeProgramacion
lenguaje = LenguajeProgramacion()

# Pedir al usuario que ingrese los datos
lenguaje.ingresar_datos()

# Imprimir la información
lenguaje.imprimir_info()

diccionario_informacion = lenguaje.imprimir_diccionario()
print("El diccionario es:",  diccionario_informacion)