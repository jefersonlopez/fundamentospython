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


# string recargado

resume = 'Python es un lenguaje de programación ampliamente utilizado'
print(len(resume))
resume = resume.upper()
print(resume)
resume = resume.lower()
print(resume)
resume = resume.title()
print(resume)
print(resume.count('p'))
resume = resume.swapcase()
print(resume)
resume = resume.capitalize()
print(resume)
resume = resume.replace('a','e')
print(resume)


#indexing y slicing

texto = "yo se python"
print(texto[1:4])
print(texto[:5])
print(texto[3:])
print(texto[::2])


#listas se puede almacenar cualquier tipo de datos no tienen que ser todos los elemnetos del mismo tipo

numbers = [1,2,3,4]
print(numbers)
print(type(numbers))

task = ['make a dishes', 'take a shower']
print(task)

task[0] = 'wake up'
print(task)


#metodos de listas

numbers = [4,6,435,432,43,23,324,3,2,5,567,65,4,2,3443,]
print(numbers)
numbers.append(6)
print(numbers)
numbers.insert(4, 45)
print(numbers)
print(numbers.index(2))
numbers.remove(23)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(10)
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
"""

#tuplas no se puede hacer cambios a estas

numbers = (1,2,3,4)
names = ('carlos', 'Juan', 'Jefersonm')
print(names.index('Juan'))
print(type(numbers))
my_list = list(numbers)
print(type(my_list))
