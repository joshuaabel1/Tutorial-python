"""
CLASE 3

Cubre operators y conditionals(if, elif y else).

"""

"Operadores aritméticos:"

# Suma
x = 2 + 3 

# Resta
y = 5 - 1

# Multiplicación
z = x * y 

# División
w = z / x 

# Módulo (resto de la división)
r = z % y 

# Exponenciación
e = 2 ** 3 

"Operadores de comparación:"

# Igualdad
x == y 

# distinto que
x != y 

# Mayor que
x > y 

# Menor que
x < y 

# Mayor o igual que
x >= y 

# Menor o igual que
x <= y 

"Operadores lógicos:"

# AND lógico
(x > 0) and (y < 10) 

# OR lógico
(x < 0) or (y > 0) 

# NOT lógico
not (x > y) 

"Condicionales:"

# Sentencia if

x = 5

if x > 0:
    print("x es positivo")

# Sentencia if-else

x = -2

if x > 0:
    print("x es positivo")
else:
    print("x es negativo o cero")

# Sentencia if-elif-else

x = 0

if x > 0:
    print("x es positivo")
elif x < 0:
    print("x es negativo")
else:
    print("x es cero")

