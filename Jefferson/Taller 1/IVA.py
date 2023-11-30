'''
Algoritmo que calcula el IVA de un producto
'''

Product = float(input("Select the price of your product "))
Amount = float(input("Select the mount of your product "))

Total = Product * Amount 

print("Your total is: ", Total)

IVA = Total * 0.16

Total_IVA = Total + IVA

print("Your total whit the IVA is: ", Total_IVA)
