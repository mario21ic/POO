package donaciones;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author mario21ic
 */
public class Administrador {
    private List<Donante> donantes = new ArrayList<Donante>();
    
    public void registrarDonante(Donante donante){
        this.donantes.add(donante);
    }
    
    public double montoTotal() {
        double total = 0.00;
        for(Donante d:donantes) {
            total += d.getMonto();
        }
        return total;
    }
    
    public String donanteTop() {
        String donanteTop = "";
        double montoAnterior = 0.00;
        for(Donante d:donantes) {
            if (d.getMonto() > montoAnterior) {
                donanteTop = d.getNombre();
            }
            montoAnterior = d.getMonto();
        }
        return donanteTop;
    }
    
    public Donante buscarDonante(String dni) {
        for(Donante d:donantes) {
            if (d.getDni() == dni) {
                return d;
            }
        }
        Donante donante = new Donante();
        return donante;
    }
    
    public double montoPromedio() {
        return (this.montoTotal() / donantes.size());
    }
}
