class Curso

    def initialize(nombre)
        @nombre = nombre
        @alumnos = []
    end

    def agregar_alumno(alumno)
        @alumnos += [alumno]
    end

    def listar_matriculados
        listado = "Curso: " + @nombre + "\n\n"
        @alumnos.each do |alumno|
            listado += alumno.to_s + "\n"
        end
        return listado
    end

end
