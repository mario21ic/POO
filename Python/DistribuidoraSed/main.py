from Proveedor import Proveedor
from ProveedorSingleton import ProveedorSingleton
from Producto import Producto
from ProductoSingleton import ProductoSingleton
from Almacen import Almacen

def main():
    proveedor_a = Proveedor("01", "Mario", "4418", "Av Inform", "mario21ic@gmail.com")
    proveedor_b = Proveedor("02", "Mirian", "4418", "Av Inform", "mirian@gmail.com")
    proveedor_singleton = ProveedorSingleton()
    proveedor_singleton.registrar(proveedor_a)
    proveedor_singleton.registrar(proveedor_b)
    print "Proveedor 01",proveedor_singleton.validar_existencia("02")

    producto_a = Producto("001", "DescripA", 12.0, proveedor_a)
    producto_b = Producto("002", "DescripB", 13.0, proveedor_a)
    producto_singleton = ProductoSingleton()
    producto_singleton.registrar(producto_a)
    producto_singleton.registrar(producto_b)
    print "Producto 001",producto_singleton.validar_existencia("001")

    almacen = Almacen()
    almacen.ingresar("001", 3)
    almacen.ingresar("001", 2)
    almacen.salir("001", 2)

    print "Stock 001: ",almacen.calcular_stock("001")
    print "Costo total: ",almacen.calcular_costo_total()

if __name__ == "__main__":
    main()
