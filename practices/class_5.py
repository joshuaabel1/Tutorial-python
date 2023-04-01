"""
CLASE 5

Cubre funciones y lambdas.

"""

# Las funciones son bloques de código reutilizables que realizan una tarea específica. 
# Aquí te muestro algunos ejemplos de funciones básicas en Python:

"Función que suma dos números: "

def sum(a, b):
    return a + b

result = sum(5, 3)
print(result)  # salida: 8

# Definimos una función llamada sum que toma dos argumentos (a y b)
# y devuelve la suma de estos dos números. Luego, llamamos a la función y asignamos 
# su resultado a la variable resultado, que luego se imprime en la consola.

"Función que devuelve la longitud de una cadena de texto: "

def length(string):
    return len(string)

text = "Hola, mundo!"
result = length(text)
print(result)  # salida: 12

# Definimos una función llamada longitud que toma una cadena
# de texto como argumento y devuelve su longitud utilizando la función incorporada
# len(). Luego, llamamos a la función con una cadena de texto y asignamos su resultado 
# a la variable resultado, que luego se imprime en la consola.

"Función que imprime el doble de un número: "

def double(number):
    print(number * 2)

double(5)  # salida: 10

# Definimos una función llamada double que toma un número como argumento
# y lo imprime multiplicado por 2. Luego, llamamos a la función con el argumento 5, 
# lo que imprimirá el valor 10 en la consola.

# Las funciones lambda son funciones anónimas que se utilizan para realizar tareas simples. 
# Aquí te muestro algunos ejemplos de funciones lambda básicas en Python:

"Función lambda que devuelve el doble de un número: "

# aca vamos a repetir la primera funcion pero con lambda

double = lambda x: x * 2

result = double(5)
print(result)  # salida: 10


# Definimos una función lambda que toma un argumento x y 
# devuelve el double de ese número. Luego, asignamos la función lambda a la 
# variable doble y llamamos a la función con el argumento 5, lo que asignará
# el valor 10 a la variable resultado.

"Función lambda que devuelve la suma de dos números: "

# Lo mismo que en la anterior funcion repetimos la funcion sum pero como una 
# funcion anonima .

summ = lambda x, y: x + y

result = summ(5, 3)
print(result)  # salida: 8

# Definimos una función lambda que toma dos argumentos (x e y) y devuelve
# la suma de esos dos números. Luego, asignamos la función lambda a la variable
# suma y llamamos a la función con los argumentos 5 y 3, lo que asignará el valor
# 8 a la variable resultado.

"Función lambda que devuelve una lista de números pares: "

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pair = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers)  # salida: [2, 4, 6, 8]

# Definimos una lista de números numbers y utilizamos la función filter junto
# con una función lambda para filtrar los números pares de la lista. La función
# lambda toma un argumento x y devuelve True si x es divisible por 2 
# (es decir, si es un número par). Luego, convertimos el resultado en una lista y 
# lo asignamos a la variable pares, que luego se imprime en la consola.