require './Mascota'

module Veterinaria
    class Perro < Mascota
        include Veterinaria
        def initialize tamanho, nombre, edad
            @tamanho = tamanho
            super nombre, edad
        end

        def perseguirLaCola
            "Mer persigo la cola"
        end

        def comunicarse
            "guau, guau"
        end

        def presentarse
            super + "perro"
        end
    end
end
