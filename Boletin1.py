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

for i in range (int(numero5), 0, -1):
    for j in range (int(numero6), 0, -1):
        if (i == j):
            print("El MCD de estos numeros es: " + str(i))
            break
    if (j == 1):
        break

#Ejercicio 8

for i in range (0, 11, +1):
    print (str(i))

#Ejercicio 9

contador = 0
for i in range (1, 100, +1):
    suma = contador + i
    contador = contador + 1
    print (str(suma))

#Ejercicio 10

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma2 = 0
contador2 = 0
for i in range (0, len(lista), +1):
    suma2 = suma2 + lista[i]
    contador2 = contador2 + 1
promedio = suma2 / contador2
print ("El promedio de la lista es: " + str(promedio))