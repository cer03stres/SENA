valor_pc = float(input("Ingrese el valor del computador"))   #Palabra reservada de entrada Input, valor pc
cantidad_pc = float(input ("Ingrese la cantidad de dinero")) #Cantidad con la que va a pagar
cantidad = int(input("Ingrese la cantidad de computadores a comprar")) #Cantidad de computadores


if cantidad > 0:
 valor = cantidad*valor_pc
 cambio = cantidad_pc - valor
 print ("El dinero a devolverse es:", cambio)
else:
 print("Tiene que ingresar una cantidad")


