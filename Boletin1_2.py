#Ejercicio 11: 

class Persona ():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

Persona1 = Persona("Juan", 30)
Persona2 = Persona("Maria", 25)

print(Persona1.nombre + "," + str(Persona1.edad))
print(Persona2.nombre + "," + str(Persona2.edad))

#Ejercicio 12: 

class Rectangulo (): 
    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura

    def area (self):
        return self.base * self.altura
    
    def perimetro (self):
        return 2 + (self.base + self.altura)

Rectangulo1 = Rectangulo(5,10)

print("Area del rectangulo 1: " + str(Rectangulo1.area()))
print("Perimetro del rectanglo 1 : " + str(Rectangulo1.perimetro()))

#Ejercicio 13 :

class Estudiante (): 
    def __init__ (self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

Estudiante1 = Estudiante("Juan", 20, "Ingenieria en Sistemas")
Estudiante2 = Estudiante("Maria", 22, "Ingenieria en Computacion")
Estudiante3 = Estudiante("Pedro", 21, "Ingenieria en Electronica")

listaEstidiantes = [Estudiante1, Estudiante2, Estudiante3]

for estudiante in listaEstidiantes:
    print(estudiante.nombre + "," + str(estudiante.edad) + "," + estudiante.curso)
    
#Ejercicio 14: 

class CuentaBancaria (): 
    
    def __init__ (self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def ingresarDinero (self, cantidadSuma):
        self.saldo += cantidadSuma
    
    def retirarDinero (self, cantidadResta):
        self.saldo -= cantidadResta

CuentaBancaria1 = CuentaBancaria("Juan", 1000)
print (str(CuentaBancaria1.titular) + " ," + str(CuentaBancaria1.saldo))

CuentaBancaria1.ingresarDinero(250)
print (str(CuentaBancaria1.titular) + " ," + str(CuentaBancaria1.saldo))

CuentaBancaria1.retirarDinero(200)
print (str(CuentaBancaria1.titular) + " ," + str(CuentaBancaria1.saldo))

#Ejercicio 15: 

class Coche (): 
    def __init__ (self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def info (self):
        print("Marca: " + self.marca + ", Modelo: " + self.modelo)

nissan = Coche("Nissan", "skyline GT-R 34")
nissan.info()