class Animal ():
    def hablar (self):
        print("El animal habla")
    
class Perro (Animal):
    def hablar (self):
        print("El perro ladra")

class Gato (Animal):
    def hablar (self):
        print("El gato maulla")
    
pitbull = Perro()
pitbull.hablar()

gatoNegro = Gato()
gatoNegro.hablar()

animal = Animal()
animal.hablar()