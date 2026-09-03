import java.util.Scanner; // class that will read data from the keyboard

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Calculator calculator = new Calculator();

        while (true){
            // Firstly the loop will show the menu to user
            System.out.println("=-=-=-=-=-Calculadora-=-=-=-=");
            System.out.println("\n1. Soma." +
                    "\n2. Subtração." +
                    "\n3. Divisão." +
                    "\n4. Multiplicação." +
                    "\n0. Sair.");
            System.out.println("Escolha uma opção: ");
            String opition = scanner.next();
            // if variable option get number 0 the loop will break
            if (opition.equals("0")){
                System.out.println("Encerrando...");
                break;
            }

            System.out.println("Digite o primeiro número: ");
            double a = scanner.nextDouble();
            System.out.println("Digite o segundo número: ");
            double b = scanner.nextDouble();

            double result = 0;

            // Here the code will try to run some this switch-cases
            try {
                switch (opition){
                    case "1":
                        result = calculator.sum(a,b);
                        break;
                    case "2":
                        result = calculator.subtract(a,b);
                        break;
                    case "3":
                        result = calculator.divide(a,b);
                        break;
                    case "4":
                        result = calculator.multiply(a,b);
                        break;
                    default:
                        System.out.println("Opção inválida!");
                        continue;

                }
            //if switch-case to has some mathematical error this part will be execute...
                //The error message will be show in the terminal and after the code continue loop
            } catch (ArithmeticException e) {
                System.out.println("Erro: " + e.getMessage());
                continue;
            }

            System.out.println("O resultado é: " + result);

        }
    }
}
