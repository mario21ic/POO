/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package test;

import org.junit.Test;
import static org.junit.Assert.*;
import practica01.Empresa;

/**
 *
 * @author proyecto
 */
public class TestPractica01 {
    
    public TestPractica01() {
    }
    
    @Test
    public void TestCalcularPagos(){
        Empresa empresaA = new Empresa("UPC", "333666777");
        
        empresaA.registrarPasos(1);
        assertEquals(500, empresaA.calcularPago());
        
        empresaA.registrarPasos(900);
        assertEquals(500, empresaA.calcularPago());
        
        empresaA.registrarPasos(1000);
        assertEquals(500, empresaA.calcularPago());
        
        empresaA.registrarPasos(1001);
        assertEquals(520, empresaA.calcularPago());
        
        empresaA.registrarPasos(1010);
        assertEquals(520, empresaA.calcularPago());
        
        empresaA.registrarPasos(1100);
        assertEquals(520, empresaA.calcularPago());
        
        empresaA.registrarPasos(1101);
        assertEquals(540, empresaA.calcularPago());
        
        empresaA.registrarPasos(1198);
        assertEquals(540, empresaA.calcularPago());
    }
}