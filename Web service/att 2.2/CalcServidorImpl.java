package calc;

import java.util.Date;
import javax.jws.WebService;

@WebService(endpointInterface = "calc.CalculadoraServer")
public class CalculadoraServerImpl implements CalculadoraServer {

  public double soma(double num1, double num2) {
    return num1 + num2;
  }

  public double subtracao(double num1, double num2) {
    return num1 - num2;
  }

  public double multiplicacao(double num1, double num2) {
    return num1 * num2;
  }

  public double divisao(double num1, double num2) {
    return num1 / num2;
  }

}