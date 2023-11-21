'''


'''

Sueldo = float(input("Ingrese su sueldo"))

if  Sueldo <= 1000: 
  precio_aplicado = Sueldo * 0.10

elif Sueldo > 1000 and Sueldo <= 2000:

 precio_aplicado = Sueldo * 0.05

elif Sueldo > 2000:
 precio_aplicado = Sueldo * 0.03

print ("sueldo con el descuento es:", Sueldo - precio_aplicado)