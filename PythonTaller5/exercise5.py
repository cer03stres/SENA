import random

class JuegoDado:
    def __init__(self):
        self.resultados = []
        self.lanzamientos = 0

    def lanzamiento_dado(self):
        #La función randint genera un número entero aleatorio
        resultado = random.randint(1, 6)
        self.resultados.append(resultado)
        self.lanzamientos += 1
        return resultado

    def ejecutar_juego(self):
        while True:
            input("Presiona Enter para lanzar el dado")
            resultado = self.lanzamiento_dado()

            print("Resultado del dado:", resultado)

            if resultado == 6:
                print(f"Felicidades, ¡has sacado un 6 en el lanzamiento número {self.lanzamientos}!")
                break

            respuesta = input("¿Quieres volver a tirar el dado? presiona S para seguir")
            if respuesta != 's':
                break

# Crear una instancia del juego
juego = JuegoDado()

# Ejecutar el juego
juego.ejecutar_juego()

# Imprimir los resultados al final
print("Resultados de los lanzamientos:", juego.resultados)