package veterinaria;

public class Ave extends Mascota {
    private String raza;

    public Ave(String nombre, int edad) {
        super(nombre, edad);
    }

    @Override
    public String comunicarse() {
        return "pio pio";
    }
    
    @Override
    public String presentarse() {
        return super.presentarse() + " ave";
    }
}
