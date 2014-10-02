class Curso(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def agregar_alumnos(self, alumno):
        self.alumnos.append(alumno)

    def listar_matriculados(self):
        listado = "Curso: " + self.nombre + "\n\n"
        for alumno in self.alumnos:
            listado += str(alumno) + "\n"
        return listado
