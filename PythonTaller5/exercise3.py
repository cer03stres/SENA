def validar_cantidades(cantidad1, cantidad2, cantidad3):
    if cantidad1 != cantidad2 and cantidad1 != cantidad3 and cantidad2 != cantidad3:
        return True
    else:
        return False

def calcular_porcentaje (cantidad1, cantidad2, cantidad3):
    total_invertido = cantidad1 + cantidad2 + cantidad3
    porcentaje1 = (cantidad1 / total_invertido)*100
    porcentaje2 = (cantidad2 / total_invertido)*100
    porcentaje3 = (cantidad3 / total_invertido)*100
    return porcentaje1,porcentaje2,porcentaje3

while True:
    cantidad1 = float(input("Ingrese la cantidad de dinero invertida por la primera persona"))
    cantidad2 = float(input("Ingrese la cantidad de dinero invertida por la segunda persona"))
    cantidad3 = float(input("Ingrese la cantidad de dinero invertida por la tercera persona"))

    if validar_cantidades(cantidad1, cantidad2, cantidad3):
        break
    else:
        print ("La cantidad de inversión debe ser diferentes. Intentalo de nuevo")
    
porcentaje = calcular_porcentaje(cantidad1,cantidad2,cantidad3)


print("Porcentaje de inversion de la primera persona: " , porcentaje)
print("Porcentaje de inversion de la segunda persona: ", porcentaje)
print("Porcentaje de inversion de la tercera persona: ", porcentaje)