package veterinaria;

import java.util.ArrayList;

public class Cliente {
    private String nombre;
    private ArrayList<Mascota> mascotas = new ArrayList<Mascota>();
    
    public void agregarMascota(Mascota mascota) {
        this.mascotas.add(mascota);
    }
    
    public String reporteMascotas() {
        String mensaje = "";
        
        for (Mascota mascota : this.mascotas) {
            mensaje += mascota.presentarse();
            mensaje += "\n";
        }
        
        return mensaje;
    }
}