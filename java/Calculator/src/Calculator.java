public class Calculator {

    // This class have the calculator functions
   public double sum(double n1, double n2){
       return n1 + n2;
   }
   public double subtract(double n1, double n2){
       return n1 - n2;
   }
   public double divide(double n1, double n2){
       if(n2 == 0) {
           throw new ArithmeticException("Não é possível dividir por zero.");
       }
       return n1 / n2;
   }
   public double multiply(double n1, double n2){
       return n1 * n2;
   }
}
