print ("Algoritmo que descuenta tu sueldo")

sueldo = float (input("Ingrese su sueldo"))

if sueldo <= 1000:
 sueldo_aplicado = sueldo * 0.10
elif sueldo > 1000 and sueldo <= 2000:
  sueldo_aplicado = sueldo * 0.05
elif sueldo > 2000:
  sueldo_aplicado = sueldo * 0.03
print ("El sueldo con el descuento aplicado es", sueldo-sueldo_aplicado)