import unittest

from Proveedor import Proveedor
from ProveedorSingleton import ProveedorSingleton
from Producto import Producto
from ProductoSingleton import ProductoSingleton
from Almacen import Almacen

class TestAlmacen(unittest.TestCase):
    proveedor_singleton = ProveedorSingleton()
    producto_singleton = ProductoSingleton()

    def setUp(self):
        proveedor_a = Proveedor("01", "Mario", "4418", "Av Inform", "mario21ic@gmail.com")
        proveedor_b = Proveedor("02", "Mirian", "4418", "Av Inform", "mirian@gmail.com")
        self.proveedor_singleton.registrar(proveedor_a)
        self.proveedor_singleton.registrar(proveedor_b)

        producto_a = Producto("001", "DescripA", 12.0, proveedor_a)
        producto_b = Producto("002", "DescripB", 13.0, proveedor_a)
        self.producto_singleton.registrar(producto_a)
        self.producto_singleton.registrar(producto_b)

    def test_validar_proveedor(self):
        self.assertEqual(True, self.proveedor_singleton.validar_existencia("02"), 'Falso')
        self.assertEqual(False, self.proveedor_singleton.validar_existencia("03"), 'Falso')

    def test_validar_producto(self):
        self.assertEqual(True, self.producto_singleton.validar_existencia("002"), 'Falso')
        self.assertEqual(False, self.producto_singleton.validar_existencia("003"), 'Falso')

    def test_almacen(self):
        almacen = Almacen()
        almacen.ingresar("001", 3)
        almacen.ingresar("001", 2)
        almacen.salir("001", 2)
        self.assertEqual(3, almacen.calcular_stock("001"), 'Stock 001')
        self.assertEqual(36.0, almacen.calcular_costo_total(), 'Costo total')

if __name__ == '__main__':
    unittest.main()
