<?php

namespace Veterinaria;

use Mascota;

class Perro extends Mascota {

    private $tamanho;

    public function __construct($tamanho, $nombre, $edad) {
        parent::__contruct($nombre, $edad);
        $this->tamanho = $tamanho;
    }

    public function perseguirLaCola() {
        return "Me persigo la cola";
    }

    public function comunicarse() {
        return "guau, guau";
    }

    public function presentarse() {
        return parent::presentarse() . " perro";
    }
}
