from Donante import Donante
from Administrador import Administrador

def main():
    admin = Administrador()
    donanteA = Donante('Juan Perez', '44489173', '971122311', 'juan.perez@gmail.com', 100)
    donanteB = Donante('Fulano Derbez', '44489172', '971122310', 'fulano@gmail.com', 80)
    donanteC = Donante('Mario IC', '44489174', '971122317', 'mario21ic@gmail.com', 120)
    donanteD = Donante('Mengano Castillo', '44489170', '971122311', 'juan.perez@gmail.com', 50)

    admin.registrar_donante(donanteA)
    admin.registrar_donante(donanteB)
    admin.registrar_donante(donanteC)
    admin.registrar_donante(donanteD)

    print "Monto total: %s" % admin.monto_total()
    print "Donante top: %s" % admin.donante_top()
    print "Donante 44489170: %s" % admin.buscar_donante('44489170').nombre
    print "Monto promedio: %s" % admin.monto_promedio()

if __name__ == '__main__':
    main()
