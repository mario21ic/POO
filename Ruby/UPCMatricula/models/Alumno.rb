class Alumno

    def initialize(codigo, nombre, apellido)
        @codigo = codigo
        @nombre = nombre
        @apellido = apellido
    end

    def to_s
        return @nombre + "  " + @apellido
    end

end
