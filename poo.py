"""
juego
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    cantidad_de_animales = 0

    def __init__(self,name):
        self.name = name
        Animal.cantidad_de_animales += 1

    @abstractmethod
    def hacer_sonido(self):
        pass

    @classmethod
    def obtejercantidadeanimales(cls):
        print(f"la cantidad actual de animales es: {cls.cantidad_de_animales}")


class Perro(Animal):
    def hacer_sonido(self):
        print("wao wao wao ")

class Gato(Animal):
    def hacer_sonido(self):
        print("miau miau")

class Gallo(Animal):
    def hacer_sonido(self):
        print("kukurukuuuuuu")


perro = Perro("dogy")
gato = Gato("michu")
gallo = Gallo("picos")

perro.hacer_sonido()

Animal.obtejercantidadeanimales()
