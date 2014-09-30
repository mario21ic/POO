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
public class Donante {
    private String nombre;
    private String dni;
    private String telefono;
    private String email;
    private double monto;

    public Donante(String nombre, String dni, String telefono, String email, double monto) {
        this.nombre = nombre;
        this.dni = dni;
        this.telefono = telefono;
        this.email = email;
        this.monto = monto;
    }

    public Donante() {
    }

    public String getNombre() {
        return nombre;
    }

    public String getDni() {
        return dni;
    }

    public String getTelefono() {
        return telefono;
    }

    public String getEmail() {
        return email;
    }

    public double getMonto() {
        return monto;
    }
}
