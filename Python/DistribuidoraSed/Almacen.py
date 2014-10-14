from ProveedorSingleton import ProveedorSingleton
from ProductoSingleton import ProductoSingleton

class Almacen(object):
    producto_proveedor = set()
    proveedor_singleton = ProveedorSingleton()
    producto_singleton = ProductoSingleton()

    def ingresar(self, codigo_producto, cantidad):
        # validar producto
        if self.producto_singleton.validar_existencia(codigo_producto):
            producto = self.producto_singleton.obtener_producto(codigo_producto)
            # validar proveedor
            if self.proveedor_singleton.validar_existencia(producto.proveedor.codigo):
                for product in self.producto_proveedor:
                    if codigo_producto == product.codigo:
                        cantidad += product.stock
                producto.stock = cantidad
                self.producto_proveedor.add(producto)
                return True
        return False


    def salir(self, codigo_producto, cantidad):
        for producto in self.producto_proveedor:
            if codigo_producto == producto.codigo:
                producto.stock -= cantidad
                return True
        return False

    def calcular_stock(self, codigo_producto):
        stock = 0.00
        for producto in self.producto_proveedor:
            if codigo_producto == producto.codigo:
                stock += producto.stock
        return stock

    def calcular_costo_total(self):
        costo = 0.00
        for producto in self.producto_proveedor:
            costo += (producto.precio * producto.stock)
        return costo
