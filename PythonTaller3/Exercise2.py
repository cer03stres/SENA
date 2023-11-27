tiempos = []
for i in range(6):
    tiempo = int(input(f"Ingrese el tiempo de la prueba {i + 1} en minutos: "))
    #El append me pone 1 elemento ingresado en el anterior input en la lista
    tiempos.append(tiempo)

#con el any se verifica  que ninguna de las pruebas sea mayores a 16min
#con el all se verifica que almenos 1 haga un tiempo menor a 10
condicion_1 = all(tiempo <= 16 for tiempo in tiempos)
condicion_2 = any(tiempo < 10 for tiempo in tiempos)
condicion_3 = sum(tiempos) / len(tiempos) <= 15

# Determinar si el atleta es apto o no
if condicion_1 and condicion_2 and condicion_3:
    print("El atleta es apto.")
else:
    print("El atleta no es apto. Debería considerar otra especialidad.")