/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package donaciones;

/**
 *
 * @author mario21ic
 */
public class Donaciones {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Administrador admin = new Administrador();
        Donante donanteA = new Donante("Juan Perez", "44489173", "971122311", "juanperez@gmail.com", 100);
        Donante donanteB = new Donante("Fulano Derbez", "44489172", "971122310", "fulano@gmail.com", 80);
        Donante donanteC = new Donante("Mario IC", "44489174", "971122317", "mario21ic@gmail.com", 120);
        Donante donanteD = new Donante("Mengano Castillo", "44489170", "971122313", "mengano@gmail.com", 50);
        admin.registrarDonante(donanteA);
        admin.registrarDonante(donanteB);
        admin.registrarDonante(donanteC);
        admin.registrarDonante(donanteD);
        
        
        System.out.println("Monto total: " + admin.montoTotal());
        System.out.println("Donante top: " + admin.donanteTop());
        
        Donante donante = admin.buscarDonante("44489170");
        System.out.println("Donante 44489170: Nombre: " + donante.getNombre()
            + " Telefono: " + donante.getTelefono() + " - Email: " + donante.getEmail());
        
        System.out.println("Monto promedio: " + admin.montoPromedio());
    }
}
