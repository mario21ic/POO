class Cliente
    def initialize nombre
        @nombre = nombre
        @mascotas = []
    end

    def agregarMascota mascota
        @mascotas.append mascota
    end
end
