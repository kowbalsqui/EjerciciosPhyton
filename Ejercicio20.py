class Empleado (): 
    def __init__ (self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        
    def salarioAnual (self):
        return self.salario * 12
    
class Gerente (Empleado):
    
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido, salario)
    
    def salarioAnual(self):
        return super().salarioAnual()

class Programador (Empleado):
    
    def __init__ (self, nombre, apellido, salario):
        super().__init__(nombre, apellido, salario)
        
    def salarioAnual(self):
        return super().salarioAnual() 
    
francisco = Gerente("Francisco", "Lopez", 50000)
print(francisco.salarioAnual())

Carlos = Programador("Carlos", "Martinez", 30000)
print(Carlos.salarioAnual())