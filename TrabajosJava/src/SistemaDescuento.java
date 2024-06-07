
import javax.swing.JOptionPane;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author pablo
 */
public class SistemaDescuento {
    
    public static void descuento()
    {
    
        int edad = Integer.parseInt(JOptionPane.showInputDialog("Ingresa la edad del cliente"));
        double valor = Double.parseDouble(JOptionPane.showInputDialog("Ingrese el valor de la compra"));
        String respuesta = (JOptionPane.showInputDialog("¿Es Cliente VIP? (S/N)")) ;
        boolean VIP = respuesta.equalsIgnoreCase("s");

        double descuento = calcularDescuento(edad, VIP, valor);
        double valorConDescuento = valor-descuento;
        double impuestoConsumo = 0.05;
        double valorConIVA = valorConDescuento * 0.19;
        double descuentoVIP = (valorConDescuento-descuento);
        
        if (valorConDescuento > 100000) {
            impuestoConsumo = valorConDescuento * impuestoConsumo;
        }
        
        System.out.println("Valor a pagar: " + valor);
        System.out.println("Valor con descuento: " + valorConDescuento);
        System.out.println("Aplica descuento VIP: " + VIP);
        System.out.println("El IVA agregado del 19% es de " + valorConIVA);
        
        if(VIP==true){
        System.out.println("Aplica descuento VIP: " + (descuentoVIP));
         System.out.println("Valor con IVA: " + (descuentoVIP+valorConIVA));
        }else
        {
        System.out.println("El valor con IVA es " + (valorConDescuento+valorConIVA));   
        }
       
        System.out.println("Impuesto al consumo: " + impuestoConsumo);
        
    }
        public static double calcularDescuento(int edad, boolean VIP, double valor ) {
        double descuento = 0;

        if (edad >= 0 && edad <= 15) {
            descuento = valor*0.13;
        } else if (edad >= 16 && edad <= 23) {
            descuento = valor*0.23;
        } else if (edad >= 24 && edad <= 49) {
            descuento = valor*0.45;
        } else if (edad > 49) {
            descuento = valor*0.67;
        }

        if (VIP) {
            descuento = valor*0.12;

        }
        
        
        if (VIP==true){

        }
       return descuento;
        }

       
   
      public static void main(String[] args) {
        
        SistemaDescuento persona = new SistemaDescuento();
        
        persona.descuento();
        
      }
}
