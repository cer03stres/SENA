print("Programa que calcula el radio")
pi = 3.1416
radio = float(input("Ingrese el radio"))
while radio < 0:
 print("Su radio no puede ser negativo")
 radio = float(input("Ingrese el radio"))
if radio > 0:
 area = pi * radio**2
 perimetro = 2*pi * radio

print(f"El area del circulo es:", area)
print(f"El Perimetro del circulo es:", perimetro)
 
 
 