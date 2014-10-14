class ProductoSingleton(object):
    productos = set()

    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

    def registrar(self, producto):
        self.productos.add(producto)

    def validar_existencia(self, codigo_producto):
        for producto in self.productos:
            if codigo_producto == producto.codigo:
                return True
        return False

    def obtener_producto(self, codigo_producto):
        for producto in self.productos:
            if codigo_producto == producto.codigo:
                return producto
        return False

