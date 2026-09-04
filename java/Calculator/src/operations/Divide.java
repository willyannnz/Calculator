package operations;

public class Divide extends Operation{
    @Override
    public double calculate(double n1, double n2) {
        if(n2 == 0) {
            throw new ArithmeticException("Não é possível dividir por zero.");
        }
        return n1 / n2;
    }

}
