module Donaciones
    class Donante
        attr_accessor :nombre, :dni, :telefono, :email, :monto
        def initialize(nombre, dni, telefono, email, monto)
            @nombre = nombre
            @dni = dni
            @telefono = telefono
            @email = email
            @monto = monto
        end
    end
end

