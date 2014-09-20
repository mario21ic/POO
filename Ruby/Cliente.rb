module Veterinaria
    class Cliente
        def initialize nombre
            @nombre = nombre
            @mascotas = Array.new
        end

        def agregarMascota mascota
            @mascotas += [mascota]
        end

        def reporteMascotas
            mensaje = ""
            @mascotas.each do |mascota|
                mensaje += mascota.presentarse() + "\n"
            end
            return mensaje
        end
    end
end
