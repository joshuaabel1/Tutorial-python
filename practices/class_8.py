"""
CLASE 8

Cubre POO y class.

"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
juan = Persona("Juan", 25)

# Llamar al método saludar de la instancia juan
juan.saludar()

# En este ejemplo, se define una clase llamada Persona. La clase tiene dos
# atributos: nombre y edad, y un método llamado saludar que imprime una cadena 
# formateada con el nombre y la edad de la persona.

# Luego, se crea una instancia de la clase Persona con el nombre juan y 
# se le asignan valores para sus atributos. Finalmente, se llama al método
# saludar de la instancia juan para imprimir el saludo.


class Electrodomestico:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def encender(self):
        print(f"{self.marca} {self.modelo} encendido.")

    def apagar(self):
        print(f"{self.marca} {self.modelo} apagado.")

class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, precio, capacidad):
        super().__init__(marca, modelo, precio)
        self.capacidad = capacidad

    def lavar(self):
        print(f"Lavando ropa en {self.marca} {self.modelo}.")

class Televisor(Electrodomestico):
    def __init__(self, marca, modelo, precio, tamaño):
        super().__init__(marca, modelo, precio)
        self.tamaño = tamaño

    def cambiar_canal(self, canal):
        print(f"Cambiando canal a {canal} en {self.marca} {self.modelo}.")


# En este ejemplo, se define una clase Electrodomestico con atributos marca,
# modelo y precio, y métodos encender y apagar. Luego, se definen dos subclases
# que heredan de Electrodomestico: Lavadora y Televisor.

# La clase Lavadora tiene un atributo adicional capacidad y un método lavar, 
# que imprime un mensaje de que se está lavando ropa.

# La clase Televisor tiene un atributo adicional tamaño y un método cambiar_canal,
# que imprime un mensaje de que se está cambiando el canal.

# Al heredar de la clase Electrodomestico, ambas subclases obtienen los métodos y 
# atributos definidos en la clase padre, pero también pueden agregar sus propios atributos
# y métodos adicionales específicos de cada subclase.