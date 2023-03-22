## Indentacion

___En Python, el bloque de código se delimita mediante la indentación, es decir, insertando espacios o tabulaciones al inicio de las líneas que conforman el bloque. Esto es diferente a otros lenguajes de programación, como Java o C, donde se utilizan llaves para delimitar el bloque. La indentación es obligatoria en Python y es importante para la estructura y legibilidad del código.___

``` python
if condicion:
    # bloque de código
    sentencia1
    sentencia2
    ...
else:
    # bloque de código
    sentencia3
    sentencia4
    ...
```
___Se puede observar que el bloque de código dentro de la estructura if está indentado hacia la derecha, lo que indica que es parte del mismo bloque y se ejecutará sólo si se cumple la condición. El bloque de código dentro de la estructura else también está indentado, pero se encuentra en un bloque de código diferente, por lo que se ejecutará si no se cumple la condición.___



## Comentarios de varias líneas

___Para escribir comentarios que ocupan varias líneas, simplemente escribe cada una de las líneas anteponiendo el carácter #:___

``` python
# Este comentario ocupa
# 2 líneas
```


___También puedes escribir un comentario en varias líneas si lo encierras entre tres comillas simples ''' o dobles """___

``` python
a = 2
'''Este comentario
también ocupa 2 líneas'''
print(a)
```

## Docstrings

___Los docstrings son un tipo de comentarios especiales que se usan para documentar un módulo, función, clase o método. En realidad son la primera sentencia de cada uno de ellos y se encierran entre tres comillas simples o dobles.___
``` python
def suma(a, b):
    """Esta función devuelve la suma de los parámetros a y b"""
    return a + b
```

## Palabras reservadas de Python

La lista de palabras reservadas es la siguiente:


``` python
and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, yield, while y with
``` 


## Reglas y convención de nombres :

___Algunas reglas y convenciones de nombres para las variables y constantes: 
Nunca use símbolos especiales como !, @, #, $, %, etc.___

___El primer carácter no puede ser un número o dígito.___

___Las constantes son colocadas dentro de módulos Python y significa que no puede ser cambiado.___

___Los nombres de constante y variable debería tener la combinación de letras en minúsculas (de a a la z) o MAYÚSCULAS (de la A a la Z) o dígitos (del 0 al 9) o un underscore (_). Por ejemplo:___
```
snake_case
MACRO_CASE
camelCase
CapWords
```
___Los nombres que comienzan con guión bajo___ (simple _ o doble __) se reservan para - variables con significado especial___