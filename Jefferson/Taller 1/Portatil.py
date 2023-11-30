'''
Dado el costo de un computador portatil y la cantidad de dinero
entregado por el cliente, calcule e imprima el cambio que debe
devolversele al cliente.
'''
print("El portatil cuesta 2000000")

portatil = 2000000
dinero_cliente = float(input("Ingrese la cantidad de dinero."))

if dinero_cliente >= portatil:
 cambio = dinero_cliente - portatil
 print("El cambio es", cambio)
else:
 print("Dinero insuficiente para realizar la compra.")

