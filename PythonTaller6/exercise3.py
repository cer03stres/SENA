import random
class Carta:
    def __init__(self, valor, palo):
        self.__valor = valor
        self.__palo = palo

    def __str__(self):
        return f"{self.__valor} de {self.__palo}"

    def get_valor(self):
        return self.__valor


class Mazo:
    def __init__(self):
        self.__cartas = []

    def crear_mazo(self):
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for palo in palos:
            for valor in valores:
                self.__cartas.append(Carta(valor, palo))

    def barajar(self):
        random.shuffle(self.__cartas)

    def repartir_carta(self):
        if len(self.__cartas) > 0:
            return self.__cartas.pop(0)
        else:
            return None


class Jugador:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mano = []

    def recibir_carta(self, carta):
        self.__mano.append(carta)

    def mostrar_mano(self):
        print(f"{self.__nombre} tiene en su mano:")
        for carta in self.__mano:
            print(carta)


class JugadorHumano(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def recibir_carta(self, carta):
        super().recibir_carta(carta)
        print(f"{self._Jugador__nombre} recibió la carta {carta}.")


class JugadorComputadora(Jugador):
    def __init__(self):
        super().__init__("Computadora")

    def recibir_carta(self, carta):
        super().recibir_carta(carta)
        print(f"La {self._Jugador__nombre} recibió una carta.")


class Juego:
    def __init__(self, jugadores):
        self.__mazo = Mazo()
        self.__jugadores = jugadores

    def iniciar_juego(self):
        self.__mazo.crear_mazo()
        self.__mazo.barajar()
        for jugador in self.__jugadores:
            carta = self.__mazo.repartir_carta()
            if carta:
                jugador.recibir_carta(carta)

    def mostrar_mano_jugadores(self):
        for jugador in self.__jugadores:
            jugador.mostrar_mano()


# Ejemplo de uso
jugador1 = JugadorHumano("Jugador 1")
jugador2 = JugadorComputadora()
jugadores = [jugador1, jugador2]

juego = Juego(jugadores)
juego.iniciar_juego()

print("Juego iniciado. Repartiendo cartas...\n")

juego.mostrar_mano_jugadores()