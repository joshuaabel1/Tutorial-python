## excepciones:

__En Python, las excepciones son errores que ocurren durante la ejecución de un programa. Cuando se produce una excepción, el programa se detiene y se muestra un mensaje de error que indica el tipo de excepción y la línea de código en la que ocurrió.__'

__Las excepciones se manejan en Python utilizando la estructura try-except. La sintaxis básica es la siguiente:__

```python
try:
    # Código que puede causar una excepción
except ExceptionType:
    # Código que se ejecutará si se produce una excepción del tipo ExceptionType
```

__En la estructura try-except, el código que puede causar una excepción se coloca dentro del bloque try, mientras que el código que se ejecutará si se produce una excepción se coloca dentro del bloque except. La excepción se especifica como un tipo de excepción en la cláusula except. Si se produce una excepción del tipo especificado, se ejecutará el bloque except.__

``` python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

__el código dentro del bloque try intenta dividir 10 por cero, lo que resulta en una excepción ZeroDivisionError.__