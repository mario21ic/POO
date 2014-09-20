package veterinaria;

public class Veterinaria {

    public static void main(String[] args) {
        Perro perro = new Perro("Chico", "Rambo", 1);
        System.out.println(perro.presentarse());
        System.out.println(perro.comunicarse());
        
        /* Una clase abstracta no se puede instanciar
        Mascota mascota = new Mascota("Fantasma", 12);
        System.out.println(mascota.comunicarse());
        */
        
        Gato gato = new Gato("Lucifer", 3);
        System.out.println(gato.presentarse());
        System.out.println(gato.aranhar());
        // Polimorfismo (poli muchas, fismo formas): muchas formas.
        System.out.println(gato.comunicarse());
        
        Gato gato2 = new Gato("Gandalf", 7);
        Cliente cliente = new Cliente();
        cliente.agregarMascota(gato);
        cliente.agregarMascota(perro);
        cliente.agregarMascota(gato2);
        //System.out.println(cliente.reporteMascotas());
        Ave ave = new Ave("Piolin", 1);
        cliente.agregarMascota(ave);
        
        Reptil reptil = new Reptil("Juancho", 1);
        cliente.agregarMascota(reptil);
        System.out.println(cliente.reporteMascotas());
    }
}
