<?php

class Administrador {
    private $_donantes = array();

    public function registrar_donante($donante) {
        $this->_donantes[] = $donante;
    }

    public function monto_total() {
        $total = 0.00;
        foreach ($this->_donantes as $donante) {
            $total += $donante->getMonto();
        }
        return $total;
    }

    public function donante_top() {
        $monto_anterior = 0.00;
        $donante_top = "";
        foreach($this->_donantes as $donante) {
            if ($donante->getMonto() > $monto_anterior) {
                $donante_top = $donante->getNombre();
            }
            $monto_anterior = $donante->getMonto();
        }
        return $donante_top;
    }

    public function buscar_donante($dni) {
        foreach($this->_donantes as $donante) {
            if ($donante->getDni() == $dni) {
                return $donante;
            }
        }
        return FALSE;
    }

    public function monto_promedio() {
        return ($this->monto_total() / count($this->_donantes));
    }
}
