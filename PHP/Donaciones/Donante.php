<?php

class Donante {
    private $nombre;
    private $dni;
    private $telefono;
    private $email;
    private $monto;

    public function __construct($nombre, $dni, $telefono, $email, $monto) {
        $this->nombre = $nombre;
        $this->dni = $dni;
        $this->telefono = $telefono;
        $this->email = $email;
        $this->monto = $monto;
    }

    public function getNombre() {
        return $this->nombre;
    }

    public function getDni() {
        return $this->dni;
    }

    public function getTelefono() {
        return $this->telefono;
    }

    public function getEmail() {
        return $this->email;
    }

    public function getMonto() {
        return $this->monto;
    }
}
