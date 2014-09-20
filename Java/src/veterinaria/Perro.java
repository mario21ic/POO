package veterinaria;

public class Perro extends Mascota {
    private String tamanho;

    public Perro(String tamanho, String nombre, int edad) {
        super(nombre, edad);
        this.tamanho = tamanho;
    }
    
    public String perseguirLaCola() {
        return "Me persigo la cola";
    }

    @Override // Flag dice que el metodo sobreescribe el metodo padre
    public String comunicarse() {
        return "guau, guau";
    }
    
    @Override // Sobre escritura del padre para agregar
    public String presentarse() {
        return super.presentarse() + " perro";
    }
}
