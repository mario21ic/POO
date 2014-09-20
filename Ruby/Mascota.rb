module Veterinaria
    class Mascota
        def initialize nombre, edad
            @nombre = nombre
            @edad = edad
        end

        def comunicarse
            raise NotImplementedError
        end

        def presentarse
            "Me llamo " + @nombre + " soy un "
        end
    end
end
