require_relative "Donante"
require_relative "Administrador"
require "test/unit"
 
class TestDonaciones < Test::Unit::TestCase

    def setup
        @admin = Donaciones::Administrador.new
        donanteA = Donaciones::Donante.new('Juan Perez', '44489173', '971122311', 'juan.perez@gmail.com', 100)
        donanteB = Donaciones::Donante.new('Fulano Derbez', '44489172', '971122310', 'fulano@gmail.com', 80)
        donanteC = Donaciones::Donante.new('Mario IC', '44489174', '971122317', 'mario21ic@gmail.com', 120)
        donanteD = Donaciones::Donante.new('Mengano Castillo', '44489170', '971122311', 'juan.perez@gmail.com', 50)
        @admin.registrar_donante(donanteA)
        @admin.registrar_donante(donanteB)
        @admin.registrar_donante(donanteC)
        @admin.registrar_donante(donanteD)
    end

    def test_monto_total
        assert_equal(350, @admin.monto_total())
    end

    def test_buscar_donante
        donante = @admin.buscar_donante('44489174')
        assert_equal("Mario IC", donante.nombre)
        assert_equal("971122317", donante.telefono)
        assert_equal("mario21ic@gmail.com", donante.email)
        assert_equal(120, donante.monto)
    end

    def test_donante_top
        assert_equal("Mario IC", @admin.donante_top())
    end

    def test_monto_promedio
        assert_equal(87.5, @admin.monto_promedio())
    end

end
