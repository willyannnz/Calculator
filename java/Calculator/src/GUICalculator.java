import javax.swing.*;
import java.awt.GridLayout;

public class GUICalculator {
    public static void main(String[] args) {
        JFrame window = new JFrame("Calculadora");
        window.setSize(300, 400);
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JTextField display = new JTextField();
        display.setEditable(false);

        window.add(display, "North");

        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(4, 3));

        // creates all 10 number buttons at once, instead of repeating the same code 10x
        String[] numbers = {"7", "8", "9", "4", "5", "6", "1", "2", "3", "0"};
        for (String number : numbers) {
            JButton button = new JButton(number);
            // 'number' can be used inside the lambda because, in a for-each loop, each
            // iteration creates a new (effectively final) variable - unlike a regular
            // indexed for loop, where the index variable changes on every iteration
            button.addActionListener(e -> display.setText(display.getText() + number));
            buttonPanel.add(button);
        }

        window.add(buttonPanel, "Center");

        window.setVisible(true);
    }
}
