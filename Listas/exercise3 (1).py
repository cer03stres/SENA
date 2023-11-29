# Crear dos listas de cinco posiciones ingresadas por el usuario
lista1 = [int(input("Ingrese un valor para la lista 1: ")) for i in range(5)]
lista2 = [int(input("Ingrese un valor para la lista 2: ")) for i in range(5)]


lista3 = []


lista3.append(sum(lista1))

multiplicacion = 1
for i in lista2:
 multiplicacion = multiplicacion * i
lista3.append(multiplicacion)

multiplicacion2 = 1
for i in lista3:
 multiplicacion2 = i*multiplicacion2

lista3.append(multiplicacion2)


lista3.append(lista3[2]/ lista3[0])

lista3.append(min(lista3[0:3]))

print("La lista 1 es:", lista1)
print("La lista 2 es:", lista2)

print("La tercera lista es:", lista3)