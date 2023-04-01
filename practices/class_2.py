"""
CLASE 2

Cubre loops.

"""

# Para utilizar un bucle for en Python, es común trabajar con una secuencia de elementos, 
# que puede ser una lista, tupla, cadena de texto u otro objeto iterable. 
# En lugar de trabajar con índices, como en algunos otros lenguajes de programación, 
# en Python es posible recorrer directamente los elementos de una secuencia utilizando 
# el bucle for.

# Lista:

fruits = ["manzana", "banana", "kiwi", "naranja"]

for fruit in fruits:
    print(fruit)


# Este bucle for recorre la lista de frutas y 
# en cada iteración imprime el valor de la variable fruta.


# Range:

for i in range(5):
    print(i)


# Este bucle for recorre los valores del rango
# range(5) (0, 1, 2, 3, 4) y en cada iteración imprime el valor de la variable i.


# Dicts:

ages = {"Juan": 25, "María": 30, "Pedro": 35}

for name, age in ages.items():
    print(name, "have", age, "years")


# Este bucle for recorre el diccionario edades y en cada iteración imprime el nombre 
# y la edad correspondiente. La función items permite obtener tanto la clave como el valor 
# del diccionario en cada iteración.


# Aca podemos hacer tareas como multiplicar, sumar y agregar tareas
# en cada iteracion.

# Ejemplo:

for i in range(5):
    print(i**2)


# Al igual que con el bucle for, para utilizar un bucle while en Python, 
# necesitamos definir una condición que se evalúe como True o False. 
# Mientras la condición sea True, el código dentro del bucle se ejecutará repetidamente.

count = 1

while count <= 5:
    print(count)
    count += 1

# En este ejemplo, utilizamos la variable contador para llevar la cuenta de los números
# que hemos imprimido hasta el momento. La condición contador <= 5 se evalúa en cada 
# iteración del bucle, y el bucle se ejecuta mientras la condición sea verdadera. 
# En cada iteración, imprimimos el valor actual de contador, y luego incrementamos 
# su valor en 1 con contador += 1.

# A diferencia del bucle for, el bucle while no está diseñado específicamente 
# para recorrer elementos de una secuencia. En lugar de eso, podemos utilizar 
# un bucle while para ejecutar un bloque de código mientras se cumpla una cierta condición. 
# En algunos casos, podemos utilizar un contador para controlar el número de 
# iteraciones del bucle.

entry = ""

while entry != "salir":
    entry = input("Ingresa un valor (escribe 'salir' para terminar): ")
    print("Ingresaste:", entry)

print("Fin del programa")

# Este bucle while solicita una entrada de usuario utilizando la función input(). 
# El bucle se ejecuta mientras la entrada del usuario no sea igual a la cadena de 
# texto "salir". En cada iteración, se imprime la entrada del usuario utilizando la función
# print(). Cuando el usuario ingresa la palabra "salir", el bucle se detiene y se imprime 
# el mensaje "Fin del programa".


limit = 10
sum = 0
count = 1

while count <= limit:
    sum += count
    count += 1

print("La suma de los números del 1 al", limit, "es:", sum)

# Este bucle while suma los números del 1 al limite utilizando la variable
# suma y el contador contador. El bucle se ejecuta mientras el valor de contador 
# sea menor o igual que limite.