## Clases:

__En Python, las clases son una forma de crear objetos que contienen atributos y métodos. Un objeto es una instancia de una clase, y contiene valores para los atributos definidos en la clase, así como los métodos que se pueden llamar para manipular el objeto.__

__La sintaxis básica para definir una clase en Python es la siguiente:__

``` python
class GenericClass:
    def __init__(self, arg1, arg2, ...):
        self.atributo1 = arg1
        self.atributo2 = arg2
        ...

    def metodo1(self, arg1, arg2, ...):
        # codigo del metodo

    def metodo2(self, arg1, arg2, ...):
        # codigo del metodo

```

__Aquí, GenericClass es el nombre que le damos a nuestra clase. El método __init__ es el constructor de la clase, que se llama automáticamente cuando se crea un nuevo objeto de la clase. El primer argumento de cualquier método de una clase es self, que se refiere al objeto en sí mismo. Los demás argumentos son los que el método necesita para hacer su trabajo.__

__Dentro del método __init__, se establecen los atributos del objeto utilizando la sintaxis self.atributo = valor. Los métodos de la clase se definen utilizando la sintaxis def metodo(self, arg1, arg2, ...): y luego se escribe el código del método.__

__Para crear un objeto de una clase, se utiliza la sintaxis objeto = GenericClass(arg1, arg2, ...). Esto llama al constructor __init__ de la clase y devuelve un objeto que se puede manipular utilizando sus atributos y métodos.__

``` python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_informacion(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años.")
```

__Podríamos crear un objeto de esta clase así:__

``` python
persona1 = Persona("Juan", 25)
```

__Y luego podríamos llamar al método imprimir_informacion así:__

``` python
persona1.imprimir_informacion()
```

__Esto imprimiría el mensaje "Mi nombre es Juan y tengo 25 años."__