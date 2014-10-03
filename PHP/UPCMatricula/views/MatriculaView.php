<?php

#require_once '../controllers/MatriculaController.php';

class MatriculaView {
    private $matriculaController;

    public function __construct() {
        $this->matriculaController = new MatriculaController();
    }

    public function matricular() {
        $opcion = '1';
        while ($opcion != '3') {
            $this->mostrarMenu();
            $opcion = $this->leerOpcion();
            $this->evaluarOpcion($opcion);
        }
    }

    public function mostrarMenu() {
        $menu = "Bienvenido al sistema\n"
              . "1 matricular alumno\n"
              . "2 listar matriculados\n"
              . "3 salir\n";
        echo $menu;
    }

    public function leerOpcion() {
        $stdin = fopen('php://stdin', 'r');
        return fgetc($stdin);
    }

    public function leerInput() {
        $stdin = fopen('php://stdin', 'r');
        return fgets($stdin, 1024);
    }

    public function evaluarOpcion($opcion) {
        if ($opcion == '1') {
            echo "Codigo: ";
            $codigo = $this->leerInput();
            echo "Nombre: ";
            $nombre = $this->leerInput();
            echo "Apellido: ";
            $apellido = $this->leerInput();
            echo $this->matriculaController->matricular($codigo, $nombre, $apellido);
        } else if ($opcion == '2') {
            echo $this->matriculaController->reporteMatricula();
        } else {
            echo "Opcion no valida";
        }
    }
}
