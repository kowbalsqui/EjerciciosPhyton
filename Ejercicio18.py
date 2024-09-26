class Vehiculo(): 
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def informacion(self):
        return "La marca del vehiculo es: " + self.marca + ", y el modelo es: " + self.modelo
        
class Coche (Vehiculo):
    
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color
    
    def informacion(self):
        return super().informacion() + ", y el color del coche es: " + self.color

class Bicicleta (Vehiculo):
    
    def __init__ (self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
    
    def informacion(self):
        return super().informacion() + ", y el tipo de bicicleta es: " + self.tipo
        
dogger = Coche("Dogger", "Challenger", "Rojo")
print(dogger.informacion())

bici = Bicicleta("Trek", "X-10", "Montaña")
print(bici.informacion())