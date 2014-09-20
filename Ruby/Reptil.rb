require './Mascota'

module Veterinaria
    class Reptil < Mascota
        def comunicarse
            "pss.. pss"
        end

        def presentarse
            super + "reptil"
        end
    end
end
