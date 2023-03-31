"""
CLASE 10

Cubre test(doctest, pytest).

"""
import doctest
from class_8 import Appliance, WashingMachine, Television

"pytest: "


def test_appliance_on(capsys):
    e = Appliance('LG', 'ABC123', 500)
    e.on()
    captured = capsys.readouterr()
    assert captured.out.strip() == "LG ABC123 turned on."

def test_appliance_off(capsys):
    e = Appliance('LG', 'ABC123', 500)
    e.off()
    captured = capsys.readouterr()
    assert captured.out.strip() == "LG ABC123 turned off."

def test_washingmachine_wash(capsys):
    l = WashingMachine('Samsung', 'DEF456', 800, 10)
    l.wash()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Washing clothes in Samsung DEF456."

def test_televisor_cambiar_canal(capsys):
    t = Television('Sony', 'GHI789', 1000, 50)
    t.change_channel(5)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Changing channel to 5 on Sony GHI789."

# En estos tests, se definen funciones separadas para cada prueba. 
# Cada función crea una instancia de la clase correspondiente y 
# llama a uno de sus métodos. Luego, la función assert se usa para verificar
# que la salida del método sea igual a un valor esperado.

"doctest: "


def length(string):
    """
    Returns the length of the input string.

    >>> length("hello")
    5
    >>> length("Python")
    6
    >>> length("")
    0
    """
    return len(string)

# En este doctest, se definen tres casos de prueba diferentes usando la 
# sintaxis >>> y .... El primer caso de prueba espera que la función length()
# devuelva 5 cuando se le pase la cadena "hello" como argumento. El segundo caso
# de prueba espera que la función devuelva 6 cuando se le pase la cadena "Python".
# El tercer caso de prueba espera que la función devuelva 0 cuando se le pase una 
# cadena vacía.

def double(num):
    """
    Returns the input number multiplied by 2.

    >>> double(2)
    4
    >>> double(5)
    10
    >>> double(-3)
    -6
    """
    return num * 2

# En este doctest, se definen tres casos de prueba diferentes que esperan
# que la función double() devuelva el resultado correcto cuando se le pase
# un número entero como argumento. El primer caso de prueba espera que la función
# devuelva 4 cuando se le pase el número 2. El segundo caso de prueba espera que
# la función devuelva 10 cuando se le pase el número 5. El tercer caso de prueba
# espera que la función devuelva -6 cuando se le pase el número -3.

if __name__ == '__main__':
    doctest.testmod()