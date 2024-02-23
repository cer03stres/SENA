class HabitacionBase:

    def __init__(self, numero, tipo, precio, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    def __str__(self):
        return f"Habitación: {self.numero}, Tipo: {self.tipo}, ${self.precio}"
    
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre}, {self.email}"

class Reservas:

    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        
    
    def __str__(self):
        return f"Reserva de {self.cliente.nombre}, para la habitación {self.habitacion.numero}, desde {self.fecha_inicio}, hasta {self.fecha_fin}"
    

class Habitacion (HabitacionBase):


    def __init__(self, numero, tipo, precio, disponible=True):
        super().__init__(numero, tipo, precio, disponible)
        self.reserva = None

    def hacer_reserva(self, cliente, fecha_inicio, fecha_fin):
        if self.disponible:
            respuesta = input(f"¿Deseas reservar la habitación {self.numero}? (S/N):")
            if respuesta.lower() == 's':
                self.reserva = Reservas(cliente, self, fecha_inicio, fecha_fin)
                self.disponible = False
                print(f"Reserva realizaca con éxito\n{self.reserva}")
            else:
                print("Reserva cancelada")
        else:
            print("Lo siento, la habitacón no está disponible para las fechas seleccionadas.")

class Hotel:

    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        print("Habitaciones disponibles ")
        for habitacion in self.habitaciones:
            if habitacion.disponible:
                print(habitacion)
            else:
                print("La habitación no está disponible")
            
            

#Ejemplo de como utilizarlo
                

cliente1 = Cliente("Juan", "jfgomez@sena.edu.co")
cliente2 = Cliente("Felipe", "jfgomez@sena.edu.co")
habitacion1= Habitacion(101, "Simple", 100, disponible=True)
habitacion2= Habitacion (100, "Double",150, disponible=False)
hotel = Hotel("Hotel ejemplo")
hotel.mostrar_habitaciones_disponibles()
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)
habitacion1.hacer_reserva(cliente1, "2023-12-01", "2023-01-02")
habitacion2.hacer_reserva(cliente2, "2023-12-01", "2023-01-02")
