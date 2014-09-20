package veterinaria;

public abstract class Mascota {
    protected String nombre; // Para que clases hijas puedan acceder
    private int edad; // Usar int porque se usa mayor o menor que
    private String raza;

    public Mascota(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    
    /*
     * Usar metodo abstracto para que hijas las implementen
     * un metodo abstracto obliga a declarar a la clase abstracta tambien
     * Concepto de "contrato de implementacion"
     */
    public abstract String comunicarse(); // En vez de maullar o ladrar
    
    public String presentarse() {
        return "Me llamo " + this.nombre + ", soy un ";
    }
}