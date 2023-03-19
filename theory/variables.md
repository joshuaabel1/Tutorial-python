### Variables:

<pre>
Las variables en Python son etiquetas que se utilizan para hacer referencia a los datos almacenados en la memoria. Cuando se crea una variable en Python, se le asigna un nombre que se utiliza para referirse al valor almacenado en ella. En lugar de pensar en una variable como un "contenedor" que almacena un valor, es más preciso pensar en ella como una etiqueta que se adhiere a un valor en la memoria.
</pre>
<pre>
Cada vez que se crea una variable en Python, se asigna un espacio en la memoria para almacenar su valor y su tipo de dato. Es decir, la variable no solo contiene el valor de la información, sino que también tiene una referencia a su tipo de dato.
</pre>



![Ejemplo de asignacion](../files/image.png)
<pre>
Se puede utilizar el nombre de la variable "edad" en el código para hacer referencia al valor almacenado en ella. Sin embargo, es importante tener en cuenta que, en realidad, lo que se almacena en la variable es una referencia a la ubicación en la memoria donde se encuentra el valor.
</pre>
Declarar variables individuales.

```
edad = 25
```
</pre>
En este caso, la variable "edad" es un objeto de tipo entero que ocupa un espacio en la memoria. Python utiliza la referencia a este objeto para acceder al valor almacenado y manipularlo si es necesario.
<pre>
<pre>
La razón por la que se considera que las variables son objetos en Python es porque, al igual que los objetos en la programación orientada a objetos, las variables en Python tienen atributos y métodos que pueden ser utilizados para manipular su valor.
</pre>
<pre>
Por ejemplo, podemos utilizar el método "upper()" en una variable de tipo cadena para convertir todas las letras en mayúsculas:
</pre>
```
nombre = "juan"
nombre_en_mayusculas = nombre.upper()
```
<pre>
En este caso, el método "upper()" se está aplicando a la variable "nombre" que es un objeto de tipo cadena y devuelve otra cadena con todas las letras en mayúsculas.
</pre>
Varias variables.

```
nombre, apellido, edad = "Luis", "Moralez", 19
print(nombre, apellido, edad)

> "Luis", "Moralez", 19
```
<pre>
Las variables en Python son locales por defecto. Esto quiere decir que las variables       definidas y utilizadas en el bloque de código de una función, sólo tienen existencia dentro de la misma, y no interfieren con otras variables del resto del código.</pre>