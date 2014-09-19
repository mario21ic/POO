from Mascota import Mascota

class Ave(Mascota):
    def comunicarse(self):
        return "pio, pio"

    def presentarse(self):
        return super(Ave, self).presentarse() + " ave"
