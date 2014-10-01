package models;

import java.util.ArrayList;

public class Curso {
    private String nombre;
    ArrayList<Alumno> alumnos = new ArrayList<Alumno>();

    public Curso(String nombre) {
        this.nombre = nombre;
    }
    
    public void agregarAlumno(Alumno alumno) {
        alumnos.add(alumno);
    }
    
    public String listarMatriculados() {
        String list = "";
        list += "Curso: " + this.nombre + "\n\n";
        for(Alumno alumno : alumnos) {
           list += alumno + "\n";
        }
        return list;
    }
}