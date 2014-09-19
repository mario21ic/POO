from abc import ABCMeta, abstractmethod

class Mascota(object):
    __metaclass__ = ABCMeta

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def comunicarse(self):
        pass

    def presentarse(self):
        return "Me llamo " + self.nombre + ", soy un "
