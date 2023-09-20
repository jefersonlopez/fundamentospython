"""
num1 =input("ingresa el primer numero: ")
num2 =input("ingresa el segundo numero: ")
num1=int(num1)
num2=int(num2)
resultado = num1 + num2
print("la suma de losnumeros es: ", resultado)
#este es el primer comentario
"""
"""
#string
my_name = "jeferson"
print("nombre ", my_name)
#imprimir el tipo de la variable
print(type(my_name))

#int
edad = 27
print("edad ", edad)
print(type(edad))

#boolean
Estado_civil = True
print("estado ", Estado_civil)
print(type(Estado_civil))

#inputs
edad = input("¿Cual es la edad? ")
print("edad es: ", edad)
print(type(edad))
"""
name = "jeferson"
last_name = 'Lopez'
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "i'm jeferson"
print(quote)

quote2 = 'she said "hello"'
print(quote2)

#format
print("Hi, my name is " + name + " and my last name " + last_name)

template = "Hi, my name is {} and my last name is {}".format(name,last_name)
print(template)

template = f"Hi, my name is {name} and my last name is {last_name}"
print(template)

var = True
var = not var
print(var)

valor1 = "andrey"
print(type(valor1))

edad = 27
print(edad)
print(f"mi edad es {edad}")

#Operadores

print(10 +10) #suma
print(10-5) #sustraccion
print(10*2) #multiplicación
print(10/2) #división
print(10%2) #residuo de división
print(10//3) #modulo de la división
print(2**3) #potenciación

#Operadores de comparación

print(7 > 3) #mayor que
print(3 < 7) #menor que
print(3 >= 2) #mayor o igual que
print(2 <= 3) # menor o igual que
print(2 == 2) #comparación igual que
print(2 != 3) # diferente que

#Comparar flotantes

x = 3.3
print(x)
y = 2.2 + 1.1
print(y)
tolerance = 0.00001
print(abs(y-x) < tolerance)

#Operadores logicos

print(True and True) # operador and las dos condiciones deben cumplirse
print(True or False) # operador or cualquiera de las condiciones se puede cumplir

#operador not

print(not True)
print(not (True and True))

# Condicionales
'''
pet = input("cual es tu mascota Favorita: ")

if pet == "perro":
    print("excelente es perro")
if pet == "gato":
    print("Excelente es un gato")
else:
    print("perdon no corresponde")
'''

number = int(input("ingresa un numero: "))
par = number % 2
if par == 0:
    print("el numero es par")
else:
    print("el numero es impar")
