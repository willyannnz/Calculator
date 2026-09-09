import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.util.Map;

public class GUICalculator {
    private static Calculator calculator = new Calculator();
    private static Double accumulatedResult = null;
    private static String pendingOperator = null;
    private static JTextField display;

    // mapping of operator symbols to their corresponding operation codes
    private static final Map<String, String> OPERATOR_MAP = Map.of(
            "+", "1",
            "-", "2",
            "/", "3",
            "*", "4"
    );

    // color palette, so every button style change happens in one place
    private static final Color COLOR_NUMBER_BG = new Color(230, 230, 235);
    private static final Color COLOR_NUMBER_FG = new Color(40, 40, 40);
    private static final Color COLOR_OPERATOR_BG = new Color(255, 149, 0);
    private static final Color COLOR_EQUALS_BG = new Color(46, 160, 67);
    private static final Color COLOR_CLEAR_BG = new Color(220, 60, 60);
    private static final Color COLOR_WHITE_FG = Color.WHITE;
    private static final Font BUTTON_FONT = new Font("Segoe UI", Font.BOLD, 20);

    // entry point: builds the GUI and wires up all the buttons
    public static void main(String[] args) {
        JFrame window = new JFrame("Calculadora");
        window.setSize(340, 480);
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.getContentPane().setBackground(Color.WHITE);

        display = new JTextField();
        display.setEditable(false);
        display.setHorizontalAlignment(JTextField.RIGHT);
        display.setFont(new Font("Segoe UI", Font.BOLD, 32));
        display.setBackground(Color.WHITE);
        display.setForeground(new Color(20, 20, 20));
        display.setBorder(new EmptyBorder(20, 15, 20, 15));
        window.add(display, "North");

        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(6, 3, 6, 6));
        buttonPanel.setBackground(Color.WHITE);
        buttonPanel.setBorder(new EmptyBorder(10, 10, 15, 10));

        // laid out sequentially (GridLayout has no column-span), so the
        // order below IS the visual order: 3 columns, 6 rows, no gaps
        buttonPanel.add(createActionButton("C", COLOR_CLEAR_BG, COLOR_WHITE_FG, e -> clearAll()));
        buttonPanel.add(createActionButton("<-", COLOR_NUMBER_BG, COLOR_NUMBER_FG, e -> backspace()));
        buttonPanel.add(createOperatorButton("/"));

        buttonPanel.add(createNumberButton("7"));
        buttonPanel.add(createNumberButton("8"));
        buttonPanel.add(createNumberButton("9"));

        buttonPanel.add(createNumberButton("4"));
        buttonPanel.add(createNumberButton("5"));
        buttonPanel.add(createNumberButton("6"));

        buttonPanel.add(createNumberButton("1"));
        buttonPanel.add(createNumberButton("2"));
        buttonPanel.add(createNumberButton("3"));

        buttonPanel.add(createOperatorButton("*"));
        buttonPanel.add(createOperatorButton("-"));
        buttonPanel.add(createOperatorButton("+"));

        buttonPanel.add(createNumberButton("0"));
        buttonPanel.add(createActionButton(".", COLOR_NUMBER_BG, COLOR_NUMBER_FG, e -> addDecimalPoint()));
        buttonPanel.add(createActionButton("=", COLOR_EQUALS_BG, COLOR_WHITE_FG, e -> performCalculation()));

        window.add(buttonPanel, "Center");

        window.setVisible(true);
    }

    // helper: builds a styled button and wires its listener, so every
    // button below is a one-liner instead of 5 lines of repeated styling
    private static JButton createActionButton(String label, Color bg, Color fg, java.awt.event.ActionListener listener) {
        JButton button = new JButton(label);
        button.setFont(BUTTON_FONT);
        button.setBackground(bg);
        button.setForeground(fg);
        button.setFocusPainted(false);
        button.setBorderPainted(false);
        button.addActionListener(listener);
        return button;
    }

    private static JButton createNumberButton(String number) {
        return createActionButton(number, COLOR_NUMBER_BG, COLOR_NUMBER_FG,
                e -> display.setText(display.getText() + number));
    }

    private static JButton createOperatorButton(String operator) {
        return createActionButton(operator, COLOR_OPERATOR_BG, COLOR_WHITE_FG,
                e -> addOperator(operator));
    }

    private static void addOperator(String operation) {
        double currentNumber = Double.parseDouble(display.getText());

        if (accumulatedResult == null) {
            accumulatedResult = currentNumber;
        } else {
            String opcao = OPERATOR_MAP.get(pendingOperator);
            accumulatedResult = calculator.calculate(opcao, accumulatedResult, currentNumber);
        }

        pendingOperator = operation;
        display.setText("");
    }

    private static void performCalculation() {
        if (pendingOperator == null) {
            display.setText("Erro: escolha uma operação");
            return;
        }

        double currentNumber = Double.parseDouble(display.getText());
        String opcao = OPERATOR_MAP.get(pendingOperator);

        try {
            double result = calculator.calculate(opcao, accumulatedResult, currentNumber);
            display.setText(String.valueOf(result));
        } catch (ArithmeticException e) {
            display.setText("Erro: " + e.getMessage());
        }

        accumulatedResult = null;
        pendingOperator = null;
    }

    private static void clearAll() {
        accumulatedResult = null;
        pendingOperator = null;
        display.setText("");
    }

    private static void backspace() {
        String currentText = display.getText();
        if (!currentText.isEmpty()) {
            display.setText(currentText.substring(0, currentText.length() - 1));
        }
    }

    private static void addDecimalPoint() {
        if (!display.getText().contains(".")) {
            display.setText(display.getText() + ".");
        }
    }
}
