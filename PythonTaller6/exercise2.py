class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def obtener_salario(self):
        return self.salario
    
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje_en_que_programa):
        super().__init__(nombre, salario)
        self.lenguaje_en_que_programa = lenguaje_en_que_programa
    
    def obtener_salario(self):
        return super().obtener_salario()

class Diseñador(Empleado):
    def __init__(self, nombre, salario, herramienta_a_utilizar):
        super().__init__(nombre, salario)
        self.herramienta_a_utilizar = herramienta_a_utilizar

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento_gerente):
        super().__init__(nombre, salario)
        self.departamento_gerente = departamento_gerente
    

    


def obtener_informacion_empleado(empleado):
    print("Nombre:", empleado.nombre)
    print("Salario:", empleado.salario)



empleado1 = Desarrollador("Dreidy", 50000, "Python")
empleado2 = Diseñador("Andres", 45000, "Photoshop")
empleado3 = Gerente("Pablo", 60000, "Desarrollo")

empleados = [empleado1, empleado2, empleado3]

for empleado in empleados:
    obtener_informacion_empleado(empleado)
print()