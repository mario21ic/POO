package controllers;

import models.Alumno;
import models.Curso;

public class MatriculaController {
    private Curso curso;
    
    public MatriculaController() {
        this.crearCurso();
    }
    
    private void crearCurso() {
        this.curso = new Curso("POO");
    }
    
    public Alumno crearAlumno(String codigo, String nombre, String apellido) {
        Alumno alumno = new Alumno(codigo, nombre, apellido);
        return alumno;
    }

    public String matricular(String codigo, String nombre, String apellido) {
        Alumno alumno = this.crearAlumno(codigo, nombre, apellido);
        this.curso.agregarAlumno(alumno);
        return "Alumno matriculado";
    }
    
    public String reporteMatricula() {
        return this.curso.listarMatriculados();
    }
}