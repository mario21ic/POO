from Mascota import Mascota

class Reptil(Mascota):
    def comunicarse(self):
        return "pss.. pss"

    def presentarse(self):
        return super(Reptil, self).presentarse() + " reptil"
