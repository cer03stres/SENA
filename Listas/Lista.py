
#Declarar una lista de números

numeros = [7, 3, 20, 9, 8]

#declarar una lista de strings

nombres = ["Juan", "Ana", "Carlos"]

#Acceder a elementos de la lista por index



print(nombres[0]) #Imprime el nombre de la posicion 0 o sea "Juan"
print(numeros[2]) #Imprime el número '3' con la posición indicada


print("Modificar elemento de la lista, en la posicion 2 cambio 3 por un 10")

#Modificar elementos de la lista

numeros[1] = 10
print (numeros)


print("Agregar elemento a la lista")
#Agregar un elemento a la lista

numeros.append(6)

print (numeros)



print("Longitud de la lista")
#Saber la Longitud de la lista con el Length

print(len(numeros))


print("Agregar un 7 en la posición 4")
#Agregar un valor en una posicion asignada, en este caso el 7 en la posición 0
numeros.insert(3, 7)

print (numeros)


print("Lista de forma Ascendente")
#Ordenar listas
numeros.sort()
print (numeros)

#Lista forma descendente

print("Lista de forma descendente")
numeros.sort(reverse=True)
print (numeros)


#Acceder a la lista 3 de la posicion 0 y dividirlo por la posicion 2
#lista3.append(lista3[0]/ lista3[2])
