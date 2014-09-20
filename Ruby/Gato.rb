require './Mascota'

module Veterinaria
    class Gato < Mascota
        def aranhar
            "Te aranho"
        end

        def comunicarse
            "miau, miau"
        end

        def presentarse
            super + "gato"
        end
    end
end
