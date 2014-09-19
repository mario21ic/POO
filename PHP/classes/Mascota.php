<?php

namespace Veterinaria;

abstract class Mascota {
    protected $nombre;
    private $edad;
    private $raza;

    public function __construct($nombre, $edad) {
        $this->nombre = $nombre;
        $this->edad = $edad;
    }

    abstract public function comunicarse();

    public function presentarse() {
        return "Me llamo " . $this->nombre + " soy un  ";
    }
}
