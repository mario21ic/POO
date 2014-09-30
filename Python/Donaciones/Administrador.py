from Donante import Donante

class Administrador(object):
    def __init__(self):
        self.donantes = []

    def registrar_donante(self, donante):
        self.donantes.append(donante)

    def monto_total(self):
        total = 0.00
        for donante in self.donantes:
            total += donante.monto
        return total

    def donante_top(self):
        donante_top = ''
        monto_anterior = 0.00

        for donante in self.donantes:
            if donante.monto > monto_anterior:
                donante_top = donante.nombre
            monto_anterior = donante.monto
        return donante_top

    def buscar_donante(self, dni):
        for donante in self.donantes:
            if donante.dni == dni:
                return donante
        return False

    def monto_promedio(self):
        return self.monto_total() / len(self.donantes)
