## Test:


### Doctest:


__Doctest es un módulo de pruebas integrado en Python que permite escribir pruebas en línea dentro de la documentación de un módulo o función. Las pruebas escritas en la documentación pueden ser ejecutadas automáticamente utilizando el módulo doctest.__

__El módulo doctest busca las pruebas dentro de la documentación, las ejecuta y verifica si los resultados coinciden con los valores esperados. Si alguna prueba falla, se muestra un mensaje de error.__

__Para escribir pruebas en línea con doctest, se utilizan las siguientes convenciones:__

- __Las pruebas se escriben en la documentación después de los docstrings y antes de la definición de la función o método.__
  
- __Las pruebas se escriben como una sesión interactiva de Python, incluyendo la entrada y la salida esperada.__
  
- __La entrada y la salida esperada se escriben como cadenas de texto y se utilizan los caracteres ">>>" para indicar la entrada y "..." para indicar la salida esperada.__

__Un ejemplo de pruebas escritas con doctest se vería así:__

``` python
def suma(a, b):
    """
    Suma dos números y devuelve el resultado.

    >>> suma(2, 3)
    5
    >>> suma(0, 0)
    0
    >>> suma(-1, 1)
    0
    """
    return a + b
```

__En este ejemplo, se han escrito tres pruebas para la función suma utilizando doctest. Cada prueba se escribe como una sesión interactiva de Python, indicando la entrada y la salida esperada. Para ejecutar las pruebas, se utiliza el siguiente código:__

``` python
import doctest

doctest.testmod()
```

__El método testmod() busca todas las pruebas dentro de los docstrings del módulo actual y las ejecuta automáticamente. Si todas las pruebas pasan, no se mostrará ningún mensaje. Si alguna prueba falla, se mostrará un mensaje de error.__

__Doctest es una forma sencilla y eficaz de escribir y ejecutar pruebas dentro de la documentación de un módulo o función en Python.__


### Pytest:


__Pytest es un marco de pruebas de software en Python que permite escribir y ejecutar pruebas de manera fácil y eficiente. Pytest puede ser utilizado para cualquier tipo de prueba de software, desde pruebas unitarias hasta pruebas de integración y pruebas de extremo a extremo.__

__Para escribir pruebas con pytest, se definen funciones de prueba que utilizan afirmaciones para verificar si el comportamiento de la función o módulo probado es correcto. Por ejemplo, una función de prueba podría verificar que la salida de una función dada es la esperada utilizando una afirmación.__

__Un ejemplo simple de una función de prueba utilizando pytest se vería así:__

``` python

def suma(a, b):
    return a + b


def test_suma():
    assert suma(2, 3) == 5
    assert suma(0, 0) == 0
    assert suma(-1, 1) == 0
```

__En este ejemplo, se define una función de prueba llamada test_suma que verifica el comportamiento de la función suma. Dentro de la función de prueba, se utilizan afirmaciones para verificar si la salida de la función es la esperada.__

__Para ejecutar las pruebas con pytest, se utiliza el siguiente comando en la línea de comandos:__
``` bash
pytest
```
__Este comando buscará automáticamente todas las funciones de prueba que comiencen con el prefijo ``` "test_" ``` y las ejecutará. Si todas las pruebas pasan, no se mostrará ningún mensaje. Si alguna prueba falla, se mostrará un mensaje de error que indica qué prueba falló y por qué.__

__Además de las afirmaciones simples, pytest ofrece una serie de características avanzadas, como parametrización de pruebas, marcadores, configuración personalizada y plugins de terceros. Esto hace que pytest sea una herramienta muy flexible y poderosa para escribir y ejecutar pruebas en Python.__