"""
CLASE 7

Cubre list, dicts Comprehensions.

"""

"Crear una lista a partir de otra lista:"

# Puedes usar una list comprehension para crear una nueva lista basada
# en una lista existente. Por ejemplo, si tienes una lista de números y quieres
# crear una nueva lista con solo los números pares, puedes hacer lo siguiente:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs_numbers = [num for num in numbers if num % 2 == 0]

# El resultado será la lista [2, 4, 6, 8, 10].


"Crear una lista a partir de una cadena:"
# Puedes usar una list comprehension para crear una lista de caracteres
# a partir de una cadena. Por ejemplo:

string = "Hola mundo"
chars = [char for char in string]

# El resultado será la lista ['H', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o'].

"Crear una lista de tuplas:"

# Puedes usar una list comprehension para crear una lista de tuplas a partir
# de dos listas existentes. Por ejemplo, si tienes dos listas de nombres y edades, 
# puedes crear una lista de tuplas que contenga cada nombre y su respectiva edad
#  de la siguiente manera:

names = ["Juan", "María", "Pedro"]
ages = [25, 30, 40]
tups = [(names, ages) for name, age in zip(names, ages)]

# El resultado será la lista [('Juan', 25), ('María', 30), ('Pedro', 40)].

"Crear un diccionario a partir de una lista:"

# Puedes usar un dictionary comprehension para crear un diccionario a partir de una lista.
# Por ejemplo, si tienes una lista de nombres y quieres crear un diccionario donde cada
# nombre es una clave y su valor es su longitud, puedes hacer lo siguiente:

names = ["Juan", "María", "Pedro"]
dict_names = {names: len(name) for name in names}

# El resultado será el diccionario {'Juan': 4, 'María': 5, 'Pedro': 5}.

# Crear un diccionario a partir de dos listas:

# Puedes usar un dictionary comprehension para crear un diccionario a partir de dos listas.
# Por ejemplo, si tienes dos listas de nombres y edades, puedes crear un diccionario que
# contenga cada nombre como clave y su respectiva edad como valor de la siguiente manera:

names = ["Juan", "María", "Pedro"]
ages = [25, 30, 40]
dict = {names[i]: ages[i] for i in range(len(names))}

# El resultado será el diccionario {'Juan': 25, 'María': 30, 'Pedro': 40}.

"Filtrar un diccionario:"

# Puedes usar un dictionary comprehension para filtrar un diccionario en función
# de alguna condición. Por ejemplo, si tienes un diccionario con nombres y edades
# y quieres crear un nuevo diccionario con solo los nombres de las personas mayores
# de 30 años, puedes hacer lo siguiente:

people = {'Juan': 25, 'María': 30, 'Pedro': 40}
greater = {name: age for name, age in people.items() if age > 30}

# El resultado será el diccionario {'Pedro': 40}.