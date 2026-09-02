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

        }
    }
}
