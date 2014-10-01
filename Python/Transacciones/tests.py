import unittest

from Empresa import Empresa

class TestCalcularPago(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa("UPC", "333666777")

    def test_calcular_pagos_500(self):
        self.empresa.registrar_pasos(1)
        self.assertEqual(500.0, self.empresa.calcular_pago(), '500')

        self.empresa.registrar_pasos(900)
        self.assertEqual(500.0, self.empresa.calcular_pago(), '500')

        self.empresa.registrar_pasos(1000)
        self.assertEqual(500.0, self.empresa.calcular_pago(), '500')

    def test_calcular_pagos_520(self):
        self.empresa.registrar_pasos(1001)
        self.assertEqual(520.0, self.empresa.calcular_pago(), '520')

        self.empresa.registrar_pasos(1010)
        self.assertEqual(520.0, self.empresa.calcular_pago(), '520')

        self.empresa.registrar_pasos(1100)
        self.assertEqual(520.0, self.empresa.calcular_pago(), '520')

    def test_calcular_pagos_540(self):
        self.empresa.registrar_pasos(1101)
        self.assertEqual(540.0, self.empresa.calcular_pago(), '540')

        self.empresa.registrar_pasos(1198)
        self.assertEqual(540.0, self.empresa.calcular_pago(), '540')

if __name__ == '__main__':
    unittest.main()
