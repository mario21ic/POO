require './Mascota'

module Veterinaria
    class Ave < Mascota
        def comunicarse
            "pio, pio"
        end

        def presentarse
            super + "ave"
        end
    end
end
