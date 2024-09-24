#Ejercicio 1:

print("Hola mundo")

#Ejercicio 2:

numero1 = input("Ingresa el primer número:")
numero2 = input("Ingresa el segundo número:")

suma = int(numero1) + int(numero2)
print("El resultado de la suma es: " + str(suma))

#Ejercicio 3: 

base = input("Ingresa la base del triangulo: ")
altura = input("Ingresa la altura del triangulo: ")

area = int(base) * int(altura) / 2
print ("El área del triangulo es: " + str(area))

#Ejercicio 4:

celsius = input("Ingresa los grados Celsius que pasaran a fahrenheit: ")

faren = int(celsius) * 9 / 5 + 32
print("Los grados Celsius pasados a Fahrenheit son: " + str(faren))

#Ejercicio 5:

numF = input("Ingrese el numero factorial ")
numero3 = 1

for i in range (1, int(numF) + 1):
    numero3 = numero3 * i
print("El factorial de " + numF + " es: " + str(numero3))

#Ejercicio 6:

numero4 = input("Ingrese el numero ")
if (int(numero4) % 2 == 0):
    print("El numero es par")
else:
    print("El numero es impar")
    
#Ejercicio 7:

numero5 = input("Ingresa un número ")
numero6 = input("Ingresa otro número ")

for i in range (int(numero5), 0 -1):
    for j in range (int(numero6), 0 -1):
        if (i == j):
            print("El MCD de estos numeros es: " + str(i))