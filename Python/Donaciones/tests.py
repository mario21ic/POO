import unittest

from Donante import Donante
from Administrador import Administrador

class TestDonaciones(unittest.TestCase):
    def setUp(self):
        self.admin = Administrador()
        donanteA = Donante('Juan Perez', '44489173', '971122311', 'juan.perez@gmail.com', 100)
        donanteB = Donante('Fulano Derbez', '44489172', '971122310', 'fulano@gmail.com', 80)
        donanteC = Donante('Mario IC', '44489174', '971122317', 'mario21ic@gmail.com', 120)
        donanteD = Donante('Mengano Castillo', '44489170', '971122311', 'juan.perez@gmail.com', 50)

        self.admin.registrar_donante(donanteA)
        self.admin.registrar_donante(donanteB)
        self.admin.registrar_donante(donanteC)
        self.admin.registrar_donante(donanteD)

    def test_monto_total(self):
        self.assertEqual(350.0, self.admin.monto_total(), 'Monto total')

    def test_donante_top(self):
        self.assertEqual("Mario IC", self.admin.donante_top(), "Donante top")

    def test_buscar_donante(self):
        donante = self.admin.buscar_donante('44489174')
        self.assertEqual("Mario IC", donante.nombre, "Nombre")
        self.assertEqual("971122317", donante.telefono, "Telefono")
        self.assertEqual('mario21ic@gmail.com', donante.email, 'Email')
        self.assertEqual(120, donante.monto, 'Monto')

    def test_monto_promedio(self):
        self.assertEqual(87.5, self.admin.monto_promedio(), 'Monto promedio')

if __name__ == '__main__':
    unittest.main()
