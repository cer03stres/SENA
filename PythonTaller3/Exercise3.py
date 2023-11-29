# Crear dos listas de cinco posiciones ingresadas por el usuario
lista1 = [int(input("Ingrese un valor para la lista 1: ")) for i in range(5)]
lista2 = [int(input("Ingrese un valor para la lista 2: ")) for i in range(5)]

# Crear una tercera lista para almacenar resultados
lista_resultados = []

# Almacenar la suma de los elementos de la lista 1 en la primera posición
lista_resultados.append(sum(lista1))


# Imprimir la tercera lista en pantalla
print("La tercera lista es:", lista_resultados)