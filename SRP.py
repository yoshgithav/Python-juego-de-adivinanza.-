"""
Docstring for SRP
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def hablar(self):
        pass

    def __str__(self):
        especie = self.__class__.__name__
        return f"{self.name} el {especie}"

class Perro(Animal):
    def hablar(self):
        return "wao wao!"

class Gato(Animal):
    def hablar(self):
        return "miauu miauu!"

class Pajaro(Animal):
    def hablar(self):
        return "Pío!"

class Vaca(Animal):
    def hablar(self):
        return "Muuu!"

class Caballo(Animal):
    def hablar(self):
        return "Hiii!"

class Persona:
    def __init__(self,mascota,amo):
        self.mascota = mascota
        self.amo = amo

    def __str__(self):
        return f"yo {self.amo} soy amo de {self.mascota}"

    def escuchar(self):
        return f"{self.amo} escucha a {self.mascota} decir:{self.mascota.hablar()}"


perro = Perro("Rex")
persona = Persona(perro,"juan")
print(persona)
