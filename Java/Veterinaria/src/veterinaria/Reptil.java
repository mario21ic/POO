package veterinaria;

public class Reptil extends Mascota {

    public Reptil(String nombre, int edad) {
        super(nombre, edad);
    }

    @Override
    public String comunicarse() {
        return "sppp spp";
    }
    
    @Override
    public String presentarse() {
        return super.presentarse() + " reptil";
    }
}
