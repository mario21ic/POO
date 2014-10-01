package views;

import controllers.MatriculaController;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class MatriculaView {
    private MatriculaController matriculaController;

    public MatriculaView() {
        matriculaController = new MatriculaController();
    }

    public void evaluarOpcion(char opcion) {
        String codigo = " ";
        String nombre = " ";
        String apellido = " ";
        // 'comilla simple un caracter
        // "comilla doble mas de uno
        if (opcion == '1') {
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            try {
                System.out.println("Ingrese el codigo: ");
                codigo = in.readLine();
                System.out.println("Ingrese el nombre: ");
                nombre = in.readLine();
                System.out.println("Ingrese el apellido: ");
                apellido = in.readLine();
            } catch (Exception e) {
            }
            // Invocamos al controller
            matriculaController.matricular(codigo, nombre, apellido);
        } else if (opcion == '2') {
            System.out.println(matriculaController.reporteMatricula());
        } else {
            System.out.println("No válido");
        }
    }
    
    public void matricular() {
        char opcion = '1';
        while (opcion != '3') {
            mostrarMenu();
            opcion = leerOpcion();
            evaluarOpcion(opcion);
        }
        
    }
    
    public char leerOpcion() {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        char opcion = ' ';
        try {
            opcion = in.readLine().charAt(0);
        } catch (Exception e) {
        }
        
        return opcion;
    }
    
    public void mostrarMenu() {
        String menu = "Bienvenido al sistema \n";
        menu += "1 para matricular a un alumno\n";
        menu += "2 para listar matriculados\n";
        menu += "3 salir\n";
        System.out.println(menu);
    }
}
