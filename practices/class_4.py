"""
CLASE 4

Cubre exceptions.

"""

# Las excepciones son utilizadas para manejar errores que pueden ocurrir durante
# la ejecución de un programa. Aquí te muestro algunos ejemplos básicos de excepciones
#  en Python:

"Excepción ZeroDivisionError:"

a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError:
    print("Error: división por cero")


# En este ejemplo, intentamos dividir a entre b, lo que daría como resultado
# una división por cero y produciría un error ZeroDivisionError. Para manejar 
# esta excepción, utilizamos una sentencia try-except para capturar el error 
# y mostrar un mensaje personalizado.

"Excepción ValueError:"

x = input("Ingrese un número: ")

try:
    x = int(x)
except ValueError:
    print("Error: debe ingresar un número entero")

# En este ejemplo, pedimos al usuario que ingrese un número a través de la función input(). 
# Si el usuario ingresa una cadena de texto que no puede ser convertida a un número entero, 
# se producirá un error ValueError. Para manejar esta excepción, utilizamos una sentencia 
# try-except para capturar el error y mostrar un mensaje personalizado.


"Excepción FileNotFoundError:"

try:
    file = open("archivo.txt", "r")
except FileNotFoundError:
    print("Error: el archivo no existe")

# En este ejemplo, intentamos abrir un archivo llamado "archivo.txt" en modo lectura ("r"). 
# Si el archivo no existe en la ruta especificada, se producirá un error FileNotFoundError.
# Para manejar esta excepción, utilizamos una sentencia try-except para capturar el error y 
# mostrar un mensaje personalizado.