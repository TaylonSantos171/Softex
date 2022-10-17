import java.io.Serializable;
import java.io.IOException;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

class produto implements Serializable {
    public String nome;
    public double preco;
    private static final long serialversionUID = 1l;

    public produto(String nome, double preco){
        this.nome = nome;
        this.preco = preco;
    }
} 

public class serializacaoedeserializacao {
  public static void main(String[] args) {
    
    produto prod = new produto("Iphone", 9873);
    System.out.println(prod);

    try { FileOutputStream out = new FileOutputStream("produtos.bytej");
    ObjectOutputStream objectoutput = new ObjectOutputStream(out);

    objectoutput.writeObject(prod);
    objectoutput.close();
    out.close();

    System.out.println("O objeto foi serializado");
    objectoutput.writeObject(objectoutput);
    objectoutput.close();
    System.out.println("O produto foi serializado!!!");

    } catch (Exception e) {
        System.out.println("Tivemos um erro");
    }

    produto prod1;

    try {  FileInputStream in = new FileInputStream("produtos,bytej");
    ObjectInputStream objectinput = new ObjectInputStream(in);

    prod1 = (produto)objectinput.readObject();
    objectinput.close();
    in.close();

    System.out.println("O objeto foi desserializado");
    System.out.println(prod1.nome);
    System.out.println(prod1.preco);
         
    } catch (Exception e) {
        System.out.println("Tivemos um erro!!!");
    }
    
  }  
}