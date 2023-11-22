def calculo_area(b, a):
    area = (b * a) / 2
    return area

base = float(input("Ingrese la base del triángulo:"))
altura = float(input("Ingrese la altura del triángulo:"))

area_triangulo = calculo_area(base, altura)

print(f"El área del triangulo es: {area_triangulo}")
