class Empresa
    def initialize(razon_social, ruc)
        @razon_social = razon_social
        @ruc = ruc
        @pasos = 0
    end

    def registrar_pasos(pasos)
        @pasos = pasos
    end

    def calcular_pago
        if @pasos <= 1000
            return 500
        end
        pasos_adicionales = ((@pasos - 1000) / 100.00).ceil
        return 500 + pasos_adicionales * 20
    end
end
