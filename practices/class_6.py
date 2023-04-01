"""
CLASE 6

Cubre datastructures (List, tuples, sets y dictionaries).

"""

"Lists: "

# Crear una lista vacía:

my_list = []

# Agregar elementos a la lista:

my_list.append("elemento1")
my_list.append("elemento2")
my_list.append("elemento3")
print(my_list)  # salida: ["elemento1", "elemento2", "elemento3"]

# Acceder a un elemento de la lista por su índice:

my_list = ["elemento1", "elemento2", "elemento3"]
print(my_list[0])  # salida: "elemento1"

# Cambiar un elemento de la lista por su índice:

my_list = ["elemento1", "elemento2", "elemento3"]
my_list[1] = "nuevo_elemento"
print(my_list)  # salida: ["elemento1", "nuevo_elemento", "elemento3"]

# Eliminar el último elemento de la my_list:

my_list = ["elemento1", "elemento2", "elemento3"]
my_list.pop()
print(my_list)  # salida: ["elemento1", "elemento2"]

# Obtener la longitud de la lista:

my_list = ["elemento1", "elemento2", "elemento3"]
print(len(my_list))  # salida: 3

# Ordenar una lista de números:

numbers = [4, 2, 1, 3, 5]
numbers.sort()
print(numbers)  # salida: [1, 2, 3, 4, 5]


"Tuplas: "

# Crear una tupla:

tuples = (1, 2, 3, 4, 5)

# Acceder a un elemento de la tupla por su índice:

tuples = (1, 2, 3, 4, 5)
print(tuples[0])  # salida: 1

# Obtener la longitud de la tupla:

tuples = (1, 2, 3, 4, 5)
print(len(tuples))  # salida: 5

# Convertir una tupla en una lista:

tuples = (1, 2, 3, 4, 5)
list = list(tuples)
print(list)  # salida: [1, 2, 3, 4, 5]

# Convertir una lista en una tupla:

list = [1, 2, 3, 4, 5]
tuples = tuple(list)
print(tuples)  # salida: (1, 2, 3, 4, 5)

# Unir dos tuplas:

tuples1 = (1, 2, 3)
tuples2 = (4, 5, 6)
tuples3 = tuples1 + tuples2
print(tuples3)  # salida: (1, 2, 3, 4, 5, 6)

# Contar la cantidad de veces que aparece un elemento en una tupla:

tuples = (1, 2, 3, 4, 5, 5, 5)
counter = tuples.count(5)
print(counter)  # salida: 3


"Sets: "

# Crear un set:

my_set = {1, 2, 3, 4, 5}

# Agregar elementos a un set:

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)  # salida: {1, 2, 3, 4, 5, 6}

# Eliminar un elemento de un set:

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)  # salida: {1, 2, 4, 5}

# Unir dos sets:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)  # salida: {1, 2, 3, 4, 5}

# Obtener la intersección de dos sets:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.intersection(set2)
print(set3)  # salida: {3}

# Obtener la diferencia de dos sets:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.difference(set2)
print(set3)  # salida: {1, 2}

# Verificar si un elemento está en un set:

mi_set = {1, 2, 3, 4, 5}
result = 3 in mi_set
print(result)  # salida: True

"Dicts: "

# Crear un diccionario:

my_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Lima"}

# Acceder a un valor por su clave:

my_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Lima"}
print(my_dict["edad"])  # salida: 30

# Agregar una clave-valor al diccionario:

my_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Lima"}
my_dict["profesion"] = "Ingeniero"
print(my_dict)  
# salida: {"nombre": "Juan", "edad": 30, "ciudad": "Lima", "profesion": "Ingeniero"}

# Eliminar una clave-valor del diccionario:

my_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Lima"}
del my_dict["ciudad"]
print(my_dict)  # salida: {"nombre": "Juan", "edad": 30}


# Obtener las claves de un diccionario:

my_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Lima"}
keys = my_dict.keys()
print(my_dict)  # salida: ["nombre", "edad", "ciudad"]

# Obtener los valores de un diccionario:

my_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Lima"}
values = my_dict.values()
print(my_dict)  # salida: ["Juan", 30, "Lima"]

# Verificar si una clave está en un diccionario:

my_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Lima"}
result = "nombre" in my_dict
print(result)  # salida: True


