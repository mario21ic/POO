package upcmatricula;

import models.Alumno;
import models.Curso;
import views.MatriculaView;

public class UPCMatricula {

    public static void main(String[] args) {
        /*
        Alumno alumno = new Alumno("1", "Carlos", "Lopez");
        Alumno mario21ic = new Alumno("2", "Mario", "Inga");
        Curso curso = new Curso("POO");
        curso.agregarAlumno(alumno);
        curso.agregarAlumno(mario21ic);
        System.out.println(curso.listarMatriculados());
        */
        MatriculaView matriculaview = new MatriculaView();
        matriculaview.matricular();
    }
}