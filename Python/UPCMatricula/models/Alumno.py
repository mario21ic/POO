class Alumno(object):
    def __init__(self, codigo, nombre, apellido):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return self.nombre + " " + self.apellido

    def __repr__(self):
        return self.nombre + " " + self.apellido
