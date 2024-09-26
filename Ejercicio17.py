class FiguraGeometrica ():
    def __init__ (self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
    
    def calculaArea (self):
        return self.ancho * self.altura
    
class Rectangulo (FiguraGeometrica):
    def __init__ (self, ancho, altura):
        super().__init__(ancho, altura)
    
    def calculaArea(self):
        return super().calculaArea()
    
class Triangulo (FiguraGeometrica):
    
    def __init__ (self, ancho, altura):
        super().__init__(ancho, altura)
    
    def calculaArea(self):
        return (self.ancho * self.altura) / 2
    
rectangulo = Rectangulo (3,6)
rectanguloArea = rectangulo.calculaArea()
print("El área del rectángulo es: " + str(rectanguloArea))

triangulo = Triangulo(6,9)
trianguloArea = triangulo.calculaArea()
print("El área del triangulo es: " + str(trianguloArea))