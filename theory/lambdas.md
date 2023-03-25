## Lambdas:

__una función lambda es una función anónima que se define sin necesidad de utilizar la palabra clave def. En lugar de eso, se utiliza la palabra clave lambda seguida de los parámetros de la función y una expresión que define lo que hace la función.__

__La sintaxis básica para definir una función lambda en Python es la siguiente:__

``` python
lambda argumentos: expresion

```

__Por ejemplo, una función lambda que devuelve el doble de su argumento se podría definir así:__

``` python
doble = lambda x: x * 2

```

__En este ejemplo, lambda x: define la función lambda, que toma un argumento x, y x * 2 es la expresión que devuelve el doble de x. La función lambda se asigna a la variable doble, que puede ser llamada como cualquier otra función.__

__Las funciones lambda se utilizan a menudo para definir funciones simples que sólo se utilizan en un lugar del código y no necesitan un nombre propio. También son muy útiles para definir funciones que se pasan como argumentos a otras funciones, como las funciones map() o filter().__

``` python
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

```

__En este ejemplo, se define una lista llamada numeros que contiene algunos números enteros. Luego, se utiliza la función map() para aplicar una función lambda que multiplica cada número por dos a cada elemento de la lista.__