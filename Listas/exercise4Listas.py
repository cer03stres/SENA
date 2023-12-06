estudiantes = int (input("Ingrese la cantidad de estudiantes")) 
contador = 0
notas = []

for i in range (estudiantes):
 notas_e = float(input(f"Ingrese la nota {i+1} (1:5) " ) )
 while notas_e < 0 or notas_e > 5:
  print("La nota debe estar en el rango de 1 a 5")
  break
 else:
  notas.append(notas_e)
  contador = contador+notas_e
  promedio = contador/estudiantes
print (notas)
promedio = contador/estudiantes
print("El promedio es:", promedio)

