import math

class Empresa(object):
    def __init__(self, razon_social, ruc):
        self.razon_social = razon_social
        self.ruc = ruc
        self.pasos = 0

    def registrar_pasos(self, pasos):
        self.pasos = pasos

    def calcular_pago(self):
        if self.pasos <= 1000:
            return 500
        pasos_adicionales = math.ceil((self.pasos - 1000) / 100.00)
        return 500 + pasos_adicionales * 20
