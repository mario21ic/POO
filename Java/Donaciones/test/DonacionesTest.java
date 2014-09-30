/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import donaciones.Administrador;
import donaciones.Donante;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.Before;

/**
 *
 * @author mario21ic
 */
public class DonacionesTest {
    Administrador admin;
    
    public DonacionesTest() {
    }
    
    @Before
    public void setUp() {
        Administrador admin = new Administrador();
        Donante donanteA = new Donante("Juan Perez", "44489173", "971122311", "juanperez@gmail.com", 100);
        Donante donanteB = new Donante("Fulano Derbez", "44489172", "971122310", "fulano@gmail.com", 80);
        Donante donanteC = new Donante("Mario IC", "44489174", "971122317", "mario21ic@gmail.com", 120);
        Donante donanteD = new Donante("Mengano Castillo", "44489170", "971122313", "mengano@gmail.com", 50);
        admin.registrarDonante(donanteA);
        admin.registrarDonante(donanteB);
        admin.registrarDonante(donanteC);
        admin.registrarDonante(donanteD);
        this.admin = admin;
    }
    
    @Test
    public void TestMontoTotal() {
        assertEquals(350, this.admin.montoTotal(), 0.00);
    }
    
    @Test
    public void TestDonanteTop() {
        assertEquals("Mario IC", this.admin.donanteTop());
    }
    
    @Test
    public void TestBuscarDonante() {
        Donante donante = this.admin.buscarDonante("44489174");
        assertEquals("Mario IC", donante.getNombre());
        assertEquals("971122317", donante.getTelefono());
        assertEquals("mario21ic@gmail.com", donante.getEmail());
        assertEquals(120, donante.getMonto(), 0.00);
    }
    
    @Test
    public void TestMontoPromedio() {
        assertEquals(87.5, this.admin.montoPromedio(), 0.00);
    }
}
