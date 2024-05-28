import random

def Dado():
    print(random.randint(1,6))

datosJugadores = []


def LeerJugadores():
    numeroJugadores = int (input("Ingrese el número de los jugadores, recuerde que debe ser entre 2 y 10 Jugadores: "))

   

    if numeroJugadores >= 2 and numeroJugadores <=10:
        monto = int (input("Ingrese el monto de cada jugador: "))
        for i in range (numeroJugadores):
            
            NombreJugadores = input(f"Ingrese el nombre del jugador {i+1}: ")

            Jugadores = {f'Nombre del Jugador {i+1}': NombreJugadores, 'monto': monto, 'puntos': 0,
                          'estado': 0, 'ronda': 0}

            datosJugadores.append(Jugadores)

           


        print(datosJugadores)
       

    else:
        print ("Error, debe ingresar entre 2 y 10 Jugadores")


def Apuesta():
    apuesta = int(input("Ingrese la apuesta que se va a hacer por ronda: "))
    while apuesta <= 0:
        print("Debe apostar un valor mayor a 0")
        apuesta = int(input("Ingrese la apuesta que se va a hacer por ronda: "))
    return apuesta


def PagarApuesta(jugador,apuesta):
    jugador['monto'] -= apuesta
    return jugador

def calcularPozo(apuesta, jugadores):
    pozo = apuesta*len(jugadores)
    print ("El pozo es", pozo)


    for jugador in jugadores:
        jugador = PagarApuesta(jugador,apuesta)
    


    return pozo

       

#Calcular Pozo , se define primero la apuesta


LeerJugadores()
bet = Apuesta()
calcularPozo(bet,datosJugadores)
print(datosJugadores)
