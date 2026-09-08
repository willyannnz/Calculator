import operations.Divide;
import operations.Operation;
import operations.Subtract;
import operations.Multiply;
import operations.Sum;

import java.util.HashMap;
import java.util.Map;

public class Calculator {
    private Map<String, Operation> operations;

    public Calculator() {
        operations = new HashMap<>();
        operations.put("1", new Sum());
        operations.put("2", new Subtract());
        operations.put("3", new Divide());
        operations.put("4", new Multiply());

    }

    public double calculate (String opcao, double a, double b){
        Operation operation = operations.get(opcao);
        return operation.calculate(a,b);
    }
}
