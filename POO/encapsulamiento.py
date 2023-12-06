def Cuentabancaria():
 def __init__(self, titular, saldo):
  #Atriubutos privados se usa el __
  # utilizamos el doble guión bajo (__) para prevenir accesos no autorizados.
  self. __titular = titular
  self. __saldo = saldo

  def obtener_saldo(self):
   return self.saldo
  
  def depositar(self, cantidad):
   if cantidad > 0:
    self.__saldo += cantidad 
    return True 
   return False
  
  def retirar(self, cantidad):
   #Si la cantidad es mayor a 0 y se cumple ésta condicion
   if cantidad > 0 <= self.__saldo:
    self.__saldo -= cantidad 
    #retorna verdadero y hace la operación
    return True
   return False


