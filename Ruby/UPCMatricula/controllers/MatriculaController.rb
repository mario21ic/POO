require_relative '../models/Alumno'
require_relative '../models/Curso'

class MatriculaController

    def initialize
        @curso = self.crear_curso("POO")
    end

    def crear_curso(nombre)
        return Curso.new(nombre)
    end

    def crear_alumno(codigo, nombre, apellido)
        return Alumno.new(codigo, nombre, apellido)
    end

    def matricular(codigo, nombre, apellido)
        alumno = self.crear_alumno(codigo, nombre, apellido)
        @curso.agregar_alumno(alumno)
        return "Alumno matriculado"
    end

    def reporte_matricula
        return @curso.listar_matriculados()
    end
    
end
