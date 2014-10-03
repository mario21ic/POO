<?php

class MatriculaController {

    private $curso;

    public function __construct() {
        $this->crearCurso();
    }

    public function crearCurso() {
        $this->curso = new Curso("POO");
    }

    public function crearAlumno($codigo, $nombre, $apellido) {
        $alumno = new Alumno($codigo, $nombre, $apellido);
        return $alumno;
    }

    public function matricular($codigo, $nombre, $apellido) {
        $alumno = new Alumno($codigo, $nombre, $apellido);
        $this->curso->agregarAlumno($alumno);
        return "Alumno matriculado";
    }

    public function reporteMatricula() {
        return $this->curso->listarMatriculados();
    }
}
