"""
CLASE 8

Cubre POO y class.

"""

class Persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
# Crear una instancia de la clase Persons
juan = Persons("Juan", 25)

# Llamar al método saludar de la instancia juan
juan.greet()

# En este ejemplo, se define una clase llamada Persona. La clase tiene dos
# atributos: nombre y edad, y un método llamado saludar que imprime una cadena 
# formateada con el nombre y la edad de la persona.

# Luego, se crea una instancia de la clase Persona con el nombre juan y 
# se le asignan valores para sus atributos. Finalmente, se llama al método
# saludar de la instancia juan para imprimir el saludo.


class Appliance:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def on(self):
        print(f"{self.brand} {self.model} turned on.")

    def off(self):
        print(f"{self.brand} {self.model} turned off.")

class WashingMachine(Appliance):
    def __init__(self, brand, model, price, capacity):
        super().__init__(brand, model, price)
        self.capacity = capacity

    def wash(self):
        print(f"Washing clothes in {self.brand} {self.model}.")

class Television(Appliance):
    def __init__(self, brand, model, price, size):
        super().__init__(brand, model, price)
        self.size = size

    def change_channel(self, channel):
        print(f"Changing channel to {channel} on {self.brand} {self.model}.")


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