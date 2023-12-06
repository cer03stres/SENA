class Cuentabancaria():
 def __init__(self, titular, saldo):
  #Atriubutos privados se usa el __
  # utilizamos el doble guión bajo (__) para prevenir accesos no autorizados.
  self. __titular = ""
  self. __saldo = saldo


 def obtener_saldo(self):
   return self.__saldo
  
 def depositar(self, cantidad):
  if cantidad > 0:
   self.__saldo += cantidad 
   return self.__saldo 
  return False
  
 def retirar(self, cantidad):
   #Si la cantidad es mayor a 0 y se cumple ésta condicion
  if cantidad > 0 <= self.__saldo:
   self.__saldo -= cantidad 
    #retorna verdadero y hace la operación
   return self.__saldo
  return False

cuentabancaria = Cuentabancaria("Andres", 500000)
print(cuentabancaria.obtener_saldo())


print(cuentabancaria.depositar(1000))
print(cuentabancaria.retirar(700))

