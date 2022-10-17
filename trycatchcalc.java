import java.util.Scanner;

public class trycatchcalc {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        try { System.out.println("digite um numero: "); 
            double num1 = entrada.nextDouble();
              System.out.println("digite outro numero: ");
            double num2 = entrada.nextDouble();
              System.out.println("informe a operação: ");
            String ope = entrada.next();

            double resul = "+".equals(ope) ? num1 + num2 : 0;
            resul = "-".equals(ope) ? num1 - num2 : resul;
            resul = "*".equals(ope) ? num1 * num2 : resul;
            resul = "/".equals(ope) ? num1 / num2 : resul;
            resul = "%".equals(ope) ? num1 % num2 : resul;

              System.out.printf("%.2f %s %.2f = %.2f ",num1, ope , num2, resul );

        entrada.close();

        } catch (Exception e) {
            System.out.println("tivemos um erro!!!!");
        }
    }
}

