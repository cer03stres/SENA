def contar_positivos_negativos(lista):
    positivos = 0
    negativos = 0
    i=0
    for numero in lista:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

    return positivos, negativos

# Solicitar al usuario que ingrese números separados por espacios
for i in range (10):

 entrada_usuario = int(input("Ingrese números separados por espacios:", {i+1} ))

# Convertir la entrada a una lista de números enteros
numeros = [int(numero) for numero in entrada_usuario.split()]

# Llamar a la función contar_positivos_negativos
positivos, negativos = contar_positivos_negativos(numeros)

# Mostrar los resultados
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)