/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package practica01;

/**
 *
 * @author proyecto
 */
public class Empresa {
    private String razonSocial;
    private String ruc;
    private int pasos;

    public Empresa(String razonSocial, String ruc) {
        this.razonSocial = razonSocial;
        this.ruc = ruc;
    }
    
    public void registrarPasos(int pasos) {
        this.pasos = pasos;
    }

    public int calcularPago(){
        int pago = 0;
        if (this.pasos <= 1000) {
            return 500;
        }
        int excedido = this.pasos - 1000;
        pago = (int) (500 + ((Math.ceil((excedido-1) / 100)+1)*20));
        return pago;
    }
}
