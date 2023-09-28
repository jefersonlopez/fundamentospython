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

person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

person['twitter'] = '@nicobytes'
print(person)

#Ciclos while

'''
counter = 0

while counter < 10:
    counter += 1
    print('valor couenter: ', counter)

counter = 0
while counter < 20:
    counter += 1
    if counter == 15:
        break
    print('valor counter: ', counter)

counter = 0
while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print('valor counter: ', counter)
'''


#ciclo for
'''
for element in range(1,21):
    print(element)


my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element) 


my_tuple = ('nico', 'Juli', 'Santi')
for element in my_tuple:
    print(element)


product = {
    'name': 'camisa',
    'price': 100,
    'stock': 89
}

for element in product:
    print(product[element])

for key, value in product.items():
    print(f"keys {key} => {value}")

print(product.items())

'''
people = [
    {
        'name': 'nico',
        'age': 34
    },
    {
        'name': 'Juan',
        'age': 45
    },
    {
        'name': 'Pedro',
        'age': 25
    }
]

for person in people:
    print(person)

for person in people:
    print(f"name: {person['name']}\nage: {person['age']}")