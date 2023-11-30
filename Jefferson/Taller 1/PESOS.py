'''
Algoritmo que devuelve 
la divisa de pesos 
a dolares y euros
'''


#Calcula el valor del dolar y la cantidad de pesos


value_dollar = float(input("Please write the value of Dollar "))

value_Euro = float(input("Please write the value of Euro "))

pesos = float(input("Please write the mount of pesos do you want chage "))


#Hace el cambio de divisa


Dolar = round(pesos / value_dollar, 2)
Euro = round(pesos / value_Euro, 2)


#Muestra en pantalla el resultado

print("Dollars" , Dolar)
print("Euros" , Euro)




