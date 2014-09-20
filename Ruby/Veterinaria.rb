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

    class Perro < Mascota
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

    class Ave < Mascota
        def comunicarse
            "pio, pio"
        end

        def presentarse
            super + "ave"
        end
    end

    class Reptil < Mascota
        def comunicarse
            "pss.. pss"
        end

        def presentarse
            super + "reptil"
        end
    end

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
