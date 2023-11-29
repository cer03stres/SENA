# Crear dos listas de cinco posiciones ingresadas por el usuario
lista1 = [int(input("Ingrese un valor para la lista 1: ")) for i in range(5)]
lista2 = [int(input("Ingrese un valor para la lista 2: ")) for i in range(5)]


lista3 = []


lista3.append(sum(lista1))

multiplicacion = 1
for i in lista2:
 multiplicacion = multiplicacion * i
lista3.append(multiplicacion)

for i in lista3:
 multiplicacion = i*multiplicacion

lista3.append(multiplicacion)

print("La tercera lista es:", lista3)