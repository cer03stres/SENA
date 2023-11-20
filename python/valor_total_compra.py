print ("VALOR DE LA COMPRA CON DESCUENTO") 
valor_compra = float(input ("Ingrese el valor de la compra"))

if valor_compra > 1000:
 descuento = valor_compra*0.20
 print ("el valor de la compra con el descuento es:", descuento) 
else: 
 print ("No se aplica descuento ya que la compra fue menor a 1000")

