class Habitacion:

    def __init__(self, numero, tipo, precio, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    #Str para convertirlo en string
    
    def __str__(self):
        return f"Habitacion {self.numero}, Tipo {self.tipo}, Precio {self.precio}"


class Cliente:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class Reservas:

    def __init__(self, habitacion, cliente, fecha_inicio, fecha_fin):
        self.habitacion = habitacion
        self.cliente = cliente
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    
    def __str__(self):
        return f"Reserva de {self.cliente.nombre}, para la habitación {self.habitacion.numero}, desde {self.fecha_inicio}, hasta {self.fecha_fin}"
    

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitacion = []

    def agregar_habitacion(self, habitacion):
        self.habitacion.append(habitacion)

    def haver_reserva(self, cliente,habitacion,fecha_inicio, fecha_fin):
        if habitacion.disponible:
            reserva = Reservas(habitacion, fecha_inicio, fecha_fin)
            habitacion.disponible = False
            print(f"Reserva realizada con exito!\n{reserva}")
        else:
            print("Lo siento, la habitación no está disponible para las fechas seleccionadas.")

    def cancelar_reserva(self, reserva):
        reserva.habitacion.disponible = True
        print("Reserva cancelada con éxito.")
        

