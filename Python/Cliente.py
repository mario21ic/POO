class Cliente(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []

    def agregarMascota(self, mascota):
        self.mascotas.append(mascota)

    def reporteMascotas(self):
        mensaje = ""
        for mascota in self.mascotas:
            mensaje += mascota.presentarse()
            mensaje += "\n"
        return mensaje

