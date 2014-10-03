<?php

class Curso {
    private $nombre;
    private $alumnos = [];

    public function __construct($nombre) {
        $this->nombre = $nombre;
    }

    public function agregarAlumno($alumno) {
        $this->alumnos[] = $alumno;
    }

    public function listarMatriculados() {
        $listado = "Curso: " . $this->nombre . "\n\n";
        foreach ($this->alumnos as $alumno) {
            $listado .= $alumno . "\n";
        }
        return $listado;
    }
}
