print ("Algoritmo para calcular factorial")
def factorial_numero (n):
 fac = 1   
 for i in range(1, n+1):
  fac = fac * i
 return fac

numero = int (input ("Ingrese el númerpo al que le quiere sacar factorial"))
factorial_de_numero = factorial_numero(numero)

print ("El factorial del número es:", factorial_de_numero)
