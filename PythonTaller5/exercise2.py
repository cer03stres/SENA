class OperacionesLista:
    #Arreglo vacio en donde se guardará la lista resultante
    def __init__(self):
        self.lista = []
    #Contador para que me acumule y me cuente los números que ingresaré a la lista
        self.contador = 0

    def ingresar_lista(self):
        longitud_lista = int(input("Ingrese la longitud de la lista.  " ))
        for i in range (longitud_lista):
         lista_contador = float(input(f"Ingrese el número {i+1} en la nueva lista ") )
         #El append para que me guarda lo que ingreso en el input anterior en la lista vacia.
         self.lista.append(lista_contador)
         self.contador += self.contador



        print("Lista ingresada:", self.lista)
        print("Suma Lista:", sum(self.lista))
        print("La longitud de la Lista es:", longitud_lista)

#Instancia
operaciones = OperacionesLista()

# Pedir al usuario que ingrese la lista y llamado a la función
operaciones.ingresar_lista()

