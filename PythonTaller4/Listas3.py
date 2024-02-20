# Crear dos listas de cinco posiciones ingresadas por el usuario
lista1 = [int(input("Ingrese un valor para la lista 1: ")) for _ in range(5)]
lista2 = [int(input("Ingrese un valor para la lista 2: ")) for _ in range(5)]

# Crear una tercera lista para almacenar resultados
lista_resultados = []

# Almacenar la suma de los elementos de la lista 1 en la primera posición
lista_resultados.append(sum(lista1))

# Almacenar la multiplicación de los elementos de la lista 2 en la segunda posición
multiplicacion_lista2 = 1
for elemento in lista2:
    multiplicacion_lista2 *= elemento
lista_resultados.append(multiplicacion_lista2)

# Almacenar la multiplicación de los valores en la posición 1 y 2 de la tercera lista en la tercera posición
lista_resultados.append(lista_resultados[0] * lista_resultados[1])

# Verificar que el denominador en la división no sea cero
if lista_resultados[0] != 0:
    # Almacenar la división de los valores en la posición 3 y 1 de la tercera lista en la cuarta posición
    lista_resultados.append(lista_resultados[2] / lista_resultados[0])
else:
    print("Error: No se puede dividir por cero.")

# Almacenar el menor de los valores en las posiciones 1, 2, 3 y 4 de la tercera lista en la quinta posición
lista_resultados.append(min(lista_resultados[0:4]))

# Imprimir la tercera lista en pantalla
print("La tercera lista es:", lista_resultados)