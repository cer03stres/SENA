'''
Un algoritmo que permite obtener el valor total de una compra con
un 20% de descuento a los clientes cuya compra supere los $1000
'''

#Definicion de variables
p = 1000
value = float(input("What is the price of the product do you want purchase?"))

#Descuento
if value > p:
  print("20% discount applies")
  discount = value * 0.20
  value_total = value - discount
  print("The value of product with 20% is: ", value_total)
else:
 print ("The value of produc is :", value)