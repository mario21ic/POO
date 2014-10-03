<?php

class Alumno {
    private $codigo;
    private $nombre;
    private $apellido;

    public function __construct($codigo, $nombre, $apellido) {
        $this->codigo = $codigo;
        $this->nombre = $nombre;
        $this->apellido = $apellido;
    }

    public function __toString() {
        return $this->nombre . "  " . $this->apellido;
    }
}
