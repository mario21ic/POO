module Donaciones
    class Administrador
        def initialize
            @donantes = []
        end

        def registrar_donante(donante)
            @donantes += [donante]
        end

        def monto_total
            total = 0.00
            @donantes.each do |donante|
                total += donante.monto
            end
            return total
        end

        def donante_top
            donante_top = ''
            monto_anterior = 0.00
            @donantes.each do |donante|
                if donante.monto > monto_anterior
                    donante_top = donante.nombre
                end
                monto_anterior = donante.monto
            end
            return donante_top
        end

        def buscar_donante(dni)
            @donantes.each do |donante|
                if donante.dni == dni
                    return donante
                end
            end
            return false
        end

        def monto_promedio
            self.monto_total() / @donantes.length
        end
    end
end
