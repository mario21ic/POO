<?php

require_once 'Mascota.php';

class Cliente {
    private $nombre;
    private $mascotas = array();

    public function __construct($nombre) {
        $this->nombre = $nombre;
    }

    public function agregarMascota($mascota) {
        $this->mascotas[] = $mascota;
    }

    public function reporteMascotas() {
        $mensaje = "";
        foreach ($this->mascotas as $mascota) {
            $mensaje = $mensaje . $mascota->presentarse() . "\n";
        }
        return $mensaje;
    }

}
