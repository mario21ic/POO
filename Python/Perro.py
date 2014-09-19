from Mascota import Mascota

class Perro(Mascota):
    def __init__(self, tamanho, nombre, edad):
        super(Perro, self).__init__(nombre, edad)
        self.tamanho = tamanho

    def perseguirLaCola(self):
        return "Me persigo la cola"

    def comunicarse(self):
        return "guau, guau"

    def presentarse(self):
        return super(Perro, self).presentarse() + " perro "
