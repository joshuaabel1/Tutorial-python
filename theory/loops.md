## Bucles:

### Bucle for:


__El for en Python es una estructura de control de flujo que se utiliza para iterar sobre una secuencia de elementos (por ejemplo, una lista, una tupla, un diccionario, etc.) y realizar una operación en cada elemento de la secuencia. La sintaxis básica de un bucle for en Python es la siguiente:__


``` python
for variable in secuencia:
    # cuerpo del bucle
```

__La variable toma el valor de cada elemento de la secuencia en cada iteración del bucle, y el cuerpo del bucle (las instrucciones que se encuentran indentadas debajo del encabezado del bucle for) se ejecutan una vez para cada elemento de la secuencia.__

__Por ejemplo, si quisieras imprimir cada elemento de una lista, podrías hacerlo con un bucle for de la siguiente manera:__

``` python
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)
```

__Esto imprimirá cada elemento de la lista en una línea separada.__

__También puedes utilizar la función range() para generar una secuencia de números en un rango determinado, como en el siguiente ejemplo:__

``` python
for i in range(1, 6):
    print(i)
```

Esto imprimirá los números del 1 al 5 en líneas separadas.

### Cuando usarlo?

__Los bucles for en Python son útiles para ejecutar una operación en cada elemento de una secuencia. Son especialmente útiles cuando no conocemos de antemano la cantidad de elementos que tendrá la secuencia, ya que permiten iterar eficientemente sobre cada elemento sin tener que escribir código repetitivo para cada uno.__


### Bucle while:

__En Python, el bucle while se utiliza para ejecutar un bloque de código repetidamente mientras se cumpla una determinada condición. El bucle while sigue ejecutando el bloque de código mientras la condición especificada sea verdadera.__

__La sintaxis básica del bucle while en Python es la siguiente:__

```
while condición:
    # Código a ejecutar mientras se cumpla la condición
```


__La condición es una expresión booleana que se evalúa antes de cada iteración del bucle. Si la condición es verdadera, el código dentro del bucle se ejecuta. Si la condición es falsa, el bucle se detiene y la ejecución continúa después del bucle.__

__Es importante tener en cuenta que si la condición nunca se vuelve falsa, el bucle while continuará ejecutándose indefinidamente, lo que se conoce como un "bucle infinito". Para evitar esto, se debe asegurar que en algún momento la condición se vuelva falsa.__

__Algunos ejemplos de uso del bucle while en Python son:__

- Realizar un cálculo iterativo hasta que se alcance una cierta precisión.
- Leer datos de entrada del usuario hasta que se ingrese una entrada válida.
- Procesar una lista de elementos mientras se cumpla cierta condición.
- Realizar una tarea de manera repetitiva hasta que se cumpla cierta condición.

__Un bucle while se utiliza en Python cuando se desea ejecutar un bloque de código repetidamente mientras se cumpla una condición determinada.__

``` python
numero = -1
while numero < 0:
    entrada = input("Ingrese un número entero positivo: ")
    if entrada.isdigit():
        numero = int(entrada)
    else:
        print("Entrada no válida. Intente de nuevo.")
print("El número ingresado es:", numero)

```