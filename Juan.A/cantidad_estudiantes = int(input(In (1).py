cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
notas = []

for i in range(cantidad_estudiantes):
    nota = float(input(f"Ingrese la nota final del estudiante {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / cantidad_estudiantes
print(f"La nota promedio del grupo es: {promedio}")