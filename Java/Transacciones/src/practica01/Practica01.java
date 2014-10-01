package practica01;

/**
 *
 * @marioinga
 */
public class Practica01 {

    public static void main(String[] args) {
        Empresa empresaA = new Empresa("Comunicore", "1234566668");
        Empresa empresaB = new Empresa("YarosLab", "1234563338");
        Empresa empresaC = new Empresa("UPC", "333666777");
        
        empresaA.registrarPasos(1000);
        System.out.println("EmpresaA: " + empresaA.calcularPago());
        
        empresaB.registrarPasos(1010);
        System.out.println("EmpresaB: " + empresaB.calcularPago());
        
        empresaC.registrarPasos(1101);
        System.out.println("EmpresaC: " + empresaC.calcularPago());
        
        empresaC.registrarPasos(1200);
        System.out.println("EmpresaC: " + empresaC.calcularPago());
    }
}
