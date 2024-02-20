
pythopesos = float(input("Ingrese los pesos que va a cambiar"))   #Palabra reservada de entrada Input
if pesos > 0:
 dolar = float(input("Ingrese los euros"))   #Palabra reservada de entrada Input
 euros = float(input("Ingrese los dolares"))   #Palabra reservada de entrada Input
 sumae = round(pesos/dolar)
 print ("El cambio a euros es:", sumae)
 sumad= round(pesos/euros)
 print ("El cambio a dolar es:", sumad)
else:
 print("Ingrese una cantidad")


