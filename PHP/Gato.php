<?php

require_once 'Mascota.php';

class Gato extends Mascota {

    public function aranhar() {
        return "Te aranho";
    }

    public function comunicarse() {
        return "miau, miau";
    }

    public function presentarse() {
        return parent::presentarse() . "gato";
    }
}
