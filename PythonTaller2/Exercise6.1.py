contador = 0

estudiantes = int (input("Ingrese la cantidad de estudiantes"))

for i in range (estudiantes):
 notas = float (input(f"Ingrese la nota de estudiante {i+1}"))
 contador = contador + notas

promedio = contador/estudiantes

print ("El promedio es:", promedio)