#dólares y euros

pesos = float(input("Ingrese la cantidad de pesos"))

dolar = float(input("Ingrese el valor del dólar ($4000)"))

euro = float(input("Ingrese el valor del euro($4450)"))

conversion_dolar = round(pesos/dolar)

print ("La conversión a dólares es:" , conversion_dolar)

conversion_euro = round(pesos/euro)

print ("La conversión de pesos a euros es:" , conversion_euro)

