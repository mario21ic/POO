from models.Alumno import Alumno
from models.Curso import Curso

class MatriculaController(object):
    def __init__(self):
        self.curso = self.crear_curso("POO")

    def crear_curso(self, nombre):
        return Curso(nombre)

    def crear_alumno(self, codigo, nombre, apellido):
        return Alumno(codigo, nombre, apellido)

    def matricular(self, codigo, nombre, apellido):
        alumno = self.crear_alumno(codigo, nombre, apellido)
        self.curso.agregar_alumnos(alumno)
        return "Alumno matriculado"

    def reporte_matricula(self):
        return self.curso.listar_matriculados()
