## Modulos:

__En Python, un módulo es un archivo con extensión .py que contiene código Python. Los módulos se utilizan para organizar y reutilizar el código, permitiendo la separación de las funcionalidades en diferentes archivos.__

__Para utilizar un módulo en un programa Python, es necesario importarlo en el código. Esto se puede hacer con la instrucción import seguida del nombre del módulo. También se puede utilizar la instrucción from seguida del nombre del módulo y la palabra clave import para importar funciones o clases específicas del módulo.__

__Una vez que se ha importado un módulo, se pueden utilizar sus funciones, clases y variables en el programa actual. Para acceder a los elementos del módulo, se utiliza la sintaxis nombre_del_modulo.elemento. Por ejemplo, si se ha importado el módulo math y se quiere utilizar la función sin, se puede llamar a math.sin().__

__Además de los módulos predefinidos que vienen con Python, es posible crear y utilizar módulos personalizados en los proyectos. Para hacer esto, simplemente se debe crear un archivo .py con el nombre del módulo y definir las funciones y clases necesarias en el archivo.__

__En resumen, los módulos en Python son archivos .py que contienen código Python que se utiliza para organizar y reutilizar el código. Se pueden importar en un programa con la instrucción import y se accede a sus elementos utilizando la sintaxis nombre_del_modulo.elemento. Los módulos personalizados también se pueden crear y utilizar en los proyectos.__


__Supongamos que tenemos un programa que necesita utilizar la función sqrt del módulo math para calcular la raíz cuadrada de un número. En este caso, podemos importar el módulo math en nuestro programa de la siguiente manera:__

``` python
import math

x = 16
raiz_cuadrada = math.sqrt(x)
print(raiz_cuadrada)
```