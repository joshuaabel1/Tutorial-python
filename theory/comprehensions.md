## Comprensiones:

__En Python, las comprensiones son una forma concisa y legible de crear listas, diccionarios o conjuntos mediante la aplicación de una expresión a cada elemento de una secuencia o iterador.__

__Existen tres tipos de comprensiones en Python:__

1) __Comprensiones de lista: Se usan para crear una lista a partir de otra secuencia o iterador. La sintaxis básica es:__

``` python
[expresion for elemento in secuencia if condicion]
```

__Donde expresion es la operación que se aplica a cada elemento de secuencia, elemento es la variable que representa a cada elemento de la secuencia, y condicion es opcional y se usa para filtrar elementos de la secuencia.__

__Por ejemplo, para crear una lista de los cuadrados de los números del 1 al 10, podrías escribir:__

``` python
cuadrados = [x**2 for x in range(1, 11)]
```

2) __Comprensiones de diccionario: Se usan para crear un diccionario a partir de otra secuencia o iterador. La sintaxis básica es:__

``` python
{clave_expresion: valor_expresion for elemento in secuencia if condicion}
```
__Donde clave_expresion y valor_expresion son las operaciones que se aplican a cada elemento de secuencia para generar las claves y valores del diccionario, elemento es la variable que representa a cada elemento de la secuencia, y condicion es opcional y se usa para filtrar elementos de la secuencia.__

__Por ejemplo, para crear un diccionario que mapea cada letra del alfabeto a su correspondiente número de índice (comenzando desde cero), podrías escribir:__

``` python
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
indices = {letra: i for i, letra in enumerate(alfabeto)}
```

3) __Comprensiones de conjunto: Se usan para crear un conjunto a partir de otra secuencia o iterador. La sintaxis básica es:__

``` python
{expresion for elemento in secuencia if condicion}
```

__Donde expresion es la operación que se aplica a cada elemento de secuencia, elemento es la variable que representa a cada elemento de la secuencia, y condicion es opcional y se usa para filtrar elementos de la secuencia.__

__Por ejemplo, para crear un conjunto de los cuadrados de los números impares del 1 al 10, podrías escribir:__

``` python
cuadrados_impares = {x**2 for x in range(1, 11) if x % 2 != 0}
```