import java.util.Scanner; // class that will read data from the keyboard

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Calculator calculator = new Calculator();

        while (true){
            System.out.println("=-=-=-=-=-Calculadora-=-=-=-=");
            System.out.println("\n1. Soma." +
                    "\n2. Subtração." +
                    "\n3. Divisão." +
                    "\n4. Multiplicação." +
                    "\n0. Sair.");
            System.out.println("Escolha uma opção: ");
            String opcao = scanner.next();
            if (opcao.equals("0")){
                System.out.println("Encerrando...");
                break;
            }

            System.out.println("Digite o primeiro número: ");
            double a = scanner.nextDouble();
            System.out.println("Digite o segundo número: ");
            double b = scanner.nextDouble();

            double result = 0;
            try {
                switch (opcao){
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
            } catch (ArithmeticException e) {
                System.out.println("Erro: " + e.getMessage());
                continue;
            }

            System.out.println("O resultado é: " + result);

        }
    }
}
