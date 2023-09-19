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