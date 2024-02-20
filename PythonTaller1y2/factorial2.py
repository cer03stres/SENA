numero = int (input ("Ingrese el número al que le quiere sacar factorial"))
fac = 1
i = 1

for i in range (1, numero+1):
 fac = fac * i

print ("El factorial del número es:", fac)