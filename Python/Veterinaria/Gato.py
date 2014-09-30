from Mascota import Mascota

class Gato(Mascota):
    def aranhar(self):
        return "Te aranho"

    def comunicarse(self):
        return "miau, miau"

    def presentarse(self):
        return super(Gato, self).presentarse() + " gato"
