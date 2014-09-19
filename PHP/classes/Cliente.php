<?php

namespace Veterinaria;

#include 'Mascota.php';

class Cliente {
    private $nombre;
    private $mascotas = array();

    public function __construct($nombre) {
        $this->nombre = $nombre;
    }

    public function agregarMascota(Mascota $mascota) {
        $this->mascotas[] = $mascota;
    }

    public function reporteMascotas() {
        $mensaje = "";
        foreach ($this->mascotas as $mascota) {
            $mensaje += mascota.presentarse();
            $mensaje += "\n";
        }
        return $mensaje;
    }

}
