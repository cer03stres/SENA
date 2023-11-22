def calcular_valor_total(valor_compra):

 if valor_compra >= 1000:
  descuento = 0.20
  descuento_aplicado = valor_compra * descuento
  valor_total = valor_compra - descuento_aplicado
  print(f"Descuento aplicado, ahorro de: {descuento_aplicado:.0f}")
 
 else:
  valor_total = valor_compra

 return valor_total

valor_compra = int(input("Ingrese con cuanto va a pagar"))

total = calcular_valor_total(valor_compra)
print(f"Total a pagar de: {total:.0f}")
