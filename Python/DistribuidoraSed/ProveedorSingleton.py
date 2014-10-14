class ProveedorSingleton(object):
    proveedores = set()

    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

    def registrar(self, proveedor):
        self.proveedores.add(proveedor)

    def validar_existencia(self, codigo_proveedor):
        for proveedor in self.proveedores:
            if codigo_proveedor == proveedor.codigo:
                return True
        return False

    def obtener_proveedor(self, codigo_proveedor):
        for proveedor in self.proveedores:
            if codigo_proveedor == proveedor.codigo:
                return proveedor
        return False
