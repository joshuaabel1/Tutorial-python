"""
CLASE 1

Cubre tips, variables y types.

"""

# Aca definimos varias varibles de distintos tipos.

greeting, number, float_number = "Hello word", 2, 2.11

# En este caso definimos la variable y su tipo, cuando definimos una variable 
# en Python se ocupan 2 espacios uno para nuestro variable y su valor y otro  
# para hace referencia a su tipo.

name:str = "Juan"

# Las anotaciones de tipo nos permiten acceder a los métodos correspondientes
# de cada tipo de datos y nos da información sobre el tipo de datos esperado.

print(greeting.lower().index("h"), number.__str__(), float_number.__int__())

# Esto nos permite poder desde las variable ver que en Python todo es un objeto.

# Tambien esto nos obliga a respetar el tipo de dato.

# print(greeting + number)

# Esto no va a dovolver este error (TypeError: can only concatenate str (not "int") to str)
# El tipado en Python puede ayudar a mejorar la calidad del código, hacer que sea más 
# fácil de entender y mantener, y facilitar la colaboración en equipo.

print(greeting + str(number))

# La manera correcta seria convirtiendo el entero a una cadena, esto se llama concatenar.
# str es parte de las funciones integradas de Python.

# Tambien podemos usar format string.

print(f"{greeting}{number}")

list1 = [1, 2, 5, 7]
list3 = [3, 8, 10]

# El código concatenará las dos listas list1y, list3

print(list1 + list3)

# Esto se debe a que el + operador se usa 
# para combinar las dos listas en una sola lista,
# donde los elementos de list3se agregan al final de list1.

# Ejercicios:

"""

Declarar variables del tipo int, str, bool y float sumarlas, multiplicarlas
y dividirlas.
investigar cuales son las operaciones no permitidas entre ellas y guardar los errores 
que nos devuelven.

"""