## Funciones:

__En Python, las funciones son bloques de código que realizan una tarea específica y pueden ser llamados desde otras partes del código. Las funciones en Python se definen utilizando la palabra clave def seguida del nombre de la función y los parámetros que acepta entre paréntesis. La sintaxis básica para definir una función es la siguiente:__

``` python
def nombre_funcion(parametro1, parametro2, ...):
    # Código que realiza la tarea de la función
    return resultado
```

__Dentro de la función se puede incluir cualquier código válido en Python, como operaciones matemáticas, operaciones de comparación, bucles, condicionales y llamadas a otras funciones. La función puede tener cero o más parámetros, que son valores que se pasan a la función cuando se llama.__

__Cuando se llama a una función en Python, se escribe el nombre de la función seguido de los argumentos entre paréntesis. Los argumentos se pasan a la función en el mismo orden en que se definen los parámetros.__

__La función puede devolver un valor utilizando la palabra clave return. El valor devuelto por la función puede ser cualquier objeto válido en Python, como un número, una cadena de texto, una lista o un diccionario.__

``` python
def suma(a, b):
    resultado = a + b
    return resultado

resultado_suma = suma(5, 7)
print(resultado_suma)
```

__las funciones en Python pueden ser muy útiles para dividir un programa en piezas más pequeñas y reutilizables, lo que hace que el código sea más fácil de mantener y entender.__