i = 1
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes"))


for i in range(1,cantidad_estudiantes+1):
 nota_estudiante = int(input(f"Ingrese la nota del estudiantes{i}"))

contador_notas = nota_estudiante+i
contador = i
promedio = contador_notas/contador
print ("El promedio es:", promedio)
