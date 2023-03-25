## Condiciones:


__Las condiciones en Python son expresiones booleanas que se evalúan en verdadero o falso. Las expresiones booleanas pueden estar formadas por operadores de comparación (como >, <, >=, <=, == y !=), operadores lógicos (como and, or y not) y variables booleanas.__

__Cuando se evalúa una condición, el resultado es una de las dos posibles opciones: verdadero (True) o falso (False). Dependiendo del resultado de la evaluación de la condición, se ejecutará un bloque de código o no.__

__Por ejemplo, en un condicional if en Python, el bloque de código indentado después de la expresión booleana se ejecutará si la expresión es verdadera. Si la expresión es falsa, el bloque de código se omitirá y se continuará ejecutando el código después del bloque `if`__

``` python
if condicion1:
    # código a ejecutar si condicion1 es verdadera
elif condicion2:
    # código a ejecutar si condicion1 es falsa y condicion2 es verdadera
else:
    # código a ejecutar si ninguna de las condiciones anteriores es verdadera

```

__Aquí hay un ejemplo de una expresión booleana simple que utiliza un operador de comparación y un condicional if.__

``` python
numero = 5

if numero > 0:
    print("El número es positivo")
else:
    print("El número es negativo o cero")
```

__En este ejemplo, la expresión booleana numero > 0 se evalúa como verdadera ya que el valor de la variable numero es mayor que cero. Por lo tanto, se ejecutará el primer bloque de código y se imprimirá "El número es positivo".__