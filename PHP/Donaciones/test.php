<?php

require_once 'Donante.php';
require_once 'Administrador.php';

class DonacionesTest extends PHPUnit_Framework_TestCase
{
    private $admin;

    protected function setUp() {
        // Arrange
        $this->admin = new Administrador();
        $donanteA = new Donante('Juan Perez', '44489173', '971122311', 'juan.perez@gmail.com', 100);
        $donanteB = new Donante('Fulano Derbez', '44489172', '971122310', 'fulano@gmail.com', 80);
        $donanteC = new Donante('Mario IC', '44489174', '971122317', 'mario21ic@gmail.com', 120);
        $donanteD = new Donante('Mengano Castillo', '44489170', '971122311', 'juan.perez@gmail.com', 50);
        
        // Act
        $this->admin->registrar_donante($donanteA);
        $this->admin->registrar_donante($donanteB);
        $this->admin->registrar_donante($donanteC);
        $this->admin->registrar_donante($donanteD);
    }

    public function testMontoTotal() {
        $this->assertEquals(350.0, $this->admin->monto_total());
    }

    public function testDonanteTop() {
        $this->assertEquals('Mario IC', $this->admin->donante_top());
    }

    public function testBuscarDonante() {
        $donante = $this->admin->buscar_donante('44489174');
        $this->assertEquals('Mario IC', $donante->getNombre());
        $this->assertEquals('971122317', $donante->getTelefono());
        $this->assertEquals('mario21ic@gmail.com', $donante->getEmail());
        $this->assertEquals(120, $donante->getMonto());
    }

    public function testMontoPromedio() {
        $this->assertEquals(87.5, $this->admin->monto_promedio());
    }
}
