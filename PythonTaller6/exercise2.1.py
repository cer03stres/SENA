class Empleado():
    def __init__(self, __nombre_empleado, __cargo, __salario):
        pass

class Desarrollador(Empleado):
    def __init__(__nombre_empleado, __cargo, __salario):
        super().__init__(__nombre_empleado, __cargo, __salario)
        print ("Andres")
    def __cargo(self):
        print ("Desarrollador")
    def __salario(self):
        print (500000)
class Diseñador(Empleado):
    def __nombre_empleado(self):
        print ("Dreidy", self.__nombre_empleado)
    def __cargo(self):
        print ("Diseñador", self.__cargo)
    def __salario(self):
        print (5000000, self.__salario)
class Gerente(Empleado):
      def __nombre_empleado(self):
        print ("Pablo", self.__nombre_empleado)
      def __cargo(self):
        print ("Gerente", self.__cargo)
      def __salario(self):
        print (500000, self.__salario)
def obtener_info_empleado(empleados):
    for empleado in empleados:
        empleado.__nombre_empleado(())
        empleado.__cargo(())
        empleado.__salario(())      

desarrollador = Desarrollador
diseñador = Diseñador
gerente = Gerente

    
obtener_info_empleado([desarrollador,diseñador,gerente])



