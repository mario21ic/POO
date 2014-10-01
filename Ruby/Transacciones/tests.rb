require_relative "Empresa"
require "test/unit"
 
class TestCalcularPago < Test::Unit::TestCase

    def setup
        @empresa = Empresa.new("UPC", "333666777")
    end

    def test_calcular_pagos_500
        @empresa.registrar_pasos(1)
        assert_equal(500.0, @empresa.calcular_pago())

        @empresa.registrar_pasos(900)
        assert_equal(500.0, @empresa.calcular_pago())

        @empresa.registrar_pasos(1000)
        assert_equal(500.0, @empresa.calcular_pago())
    end

    def test_calcular_pagos_520
        @empresa.registrar_pasos(1001)
        assert_equal(520.0, @empresa.calcular_pago())

        @empresa.registrar_pasos(1010)
        assert_equal(520.0, @empresa.calcular_pago())

        @empresa.registrar_pasos(1100)
        assert_equal(520.0, @empresa.calcular_pago())
    end

    def test_calcular_pagos_540
        @empresa.registrar_pasos(1101)
        assert_equal(540.0, @empresa.calcular_pago())

        @empresa.registrar_pasos(1198)
        assert_equal(540.0, @empresa.calcular_pago())
    end

end
