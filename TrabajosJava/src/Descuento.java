
import javax.swing.JOptionPane;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author pablo
 */
public class Descuento {
    
    public void Persona ()
    {
    
        double saldoTotal;
        double saldoTotalVIP;
        double descuento;
        double descuentoConVIP;
        double descuentoConsumo;
        int edad = Integer.parseInt(JOptionPane.showInputDialog("Ingresa tu Edad"));
        double valor = Double.parseDouble(JOptionPane.showInputDialog("Ingrese el monto que quiere gastar"));
        System.out.print("Opcion VIP\n.");
        System.out.print("1 VIP\n.");
        System.out.print("2 CONTINUAR\n");
        
        int VIP = Integer.parseInt(JOptionPane.showInputDialog("Ingrese 1 para VIP o 2 para continuar"));
  
              if (edad>=0 && edad<=15 && VIP == 1 ){
                descuento = (double) (valor*0.13);
                saldoTotal = (valor-descuento);
                descuentoConVIP = (double)(saldoTotal*0.12);
                descuentoConsumo = (double)((saldoTotal-descuentoConVIP)*0.05);
                System.out.println("\nSu descuento es\n ");
                System.out.print(descuento);
                System.out.println("\nSu saldo total es de\n ");
                System.out.print(saldoTotal);
                System.out.println("\nSu descuento por ser VIP es de\n");
                System.out.print(descuentoConVIP);
                System.out.println("\nSu saldo Total es de\n ");
                System.out.print(saldoTotal-descuentoConVIP);
                if (valor > 100000){
                System.out.println("\nSu descuento con impuesto al consumo es \n ");
                System.out.print(descuentoConsumo);
                System.out.println("\nSu saldo total con impuesto al consumo es \n ");
                System.out.print(saldoTotal-descuentoConVIP-descuentoConsumo);
                }
                }else{
                descuento = (double) (valor*0.13);
                saldoTotal = (valor-descuento);
                System.out.println("\nSu descuento es\n ");
                System.out.print(descuento); 
                System.out.println("\nSu saldo total es de\n ");
                System.out.print(saldoTotal);
              }if (valor > 100000){
                descuentoConsumo = (double)((saldoTotal)*0.05);
                System.out.println("\nSu descuento con impuesto al consumo es \n ");
                System.out.print(descuentoConsumo);
                System.out.println("\nSu saldo total con impuesto al consumo es \n ");
                System.out.print(saldoTotal-descuentoConsumo);
                }
            

              
           
}           
                
        
    
    
    public static void main(String[] args) {
        
        Descuento persona = new Descuento();
        
        persona.Persona();
        
        
  
    }       
}
