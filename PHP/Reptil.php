<?php

require_once 'Mascota.php';

class Reptil extends Mascota {

    public function comunicarse() {
        return "pss.. pss";
    }

    public function presentarse() {
        return parent::presentarse() . "reptil";
    }
}
