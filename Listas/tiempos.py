tiempos = [int(input(f"Ingrese el tiempo del dia {i+1} en minutos:"))for i in range(6)]

condicion1 = all(tiempo <= 16 for tiempo in tiempos)
condicion2 = any(tiempo < 10 for tiempo in tiempos)
condicion3 = sum(tiempos) / len(tiempos) <= 15
promedio = round(sum(tiempos)/len(tiempos), 2)

if condicion1 and condicion2 and condicion3:
 print ("El atleta es apto")
else:
 print("El atleta no es apto")

print ("El promedio es", promedio)