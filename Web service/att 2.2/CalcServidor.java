package calc;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;

@WebService
@SOAPBinding(style = Style.RPC)
public interface CalculadoraServer {
  @WebMethod double soma(double num1, double num2);
  @WebMethod double subtracao(double num1, double num2);
  @WebMethod double multiplicacao(double num1, double num2);
  @WebMethod double divisao(double num1, double num2);
}