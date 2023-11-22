costo = int(input("Ingrese el valor del producto"))
cantidad = int(input("Ingrese la cantidad"))
total_a_pagar = int (cantidad * costo)
iva = 0.16
total_con_iva = int (total_a_pagar * iva)
print ("El total sin iva es:", total_a_pagar)
print ("El total con iva es:", total_con_iva + total_a_pagar)