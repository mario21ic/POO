<?php

require_once 'Mascota.php';

class Ave extends Mascota {

    public function comunicarse() {
        return "pio, pio";
    }

    public function presentarse() {
        return parent::presentarse() . "ave";
    }
}
