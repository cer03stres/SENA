import random

def Dado():
    print(random.randint(1,6))

datosJugadores = []

def LeerJugadores():
    numeroJugadores = int (input("Ingrese el número de los jugadores, recuerde que deben 2 o mas: "))

   

    if numeroJugadores >= 2:
        monto = int (input("Ingrese el monto a apostar: "))
        for i in range (numeroJugadores):
            
            NombreJugadores = input(f"Ingrese el nombre del jugador {i+1}: ")

            Jugadores = {f'Nombre del Jugador {i+1}': NombreJugadores, 'monto': monto, 'puntos': 0,
                          'estado': 0, 'ronda': {i}}

            datosJugadores.append(Jugadores)

        print(datosJugadores)
    

    
    else:
        print ("Error, debe ingresar 2 o mas jugadores")


    
    
LeerJugadores()



    
   