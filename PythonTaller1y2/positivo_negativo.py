def contar_positivos_negativos(lista):
    positivos = 0
    negativos = 0
    ceros = 0

    for numero in lista:
        if numero > 0:
            positivos = positivos+1
        elif numero < 0:
            negativos = negativos+1
        elif numero == 0:
            ceros = ceros+1

    return positivos, negativos, ceros

# Ejemplo de uso
numeros = [1, -2, 3, -4, 5, -6, 7, -8, 9, 0]
positivos, negativos, ceros = contar_positivos_negativos(numeros)

print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números negativos:", ceros)