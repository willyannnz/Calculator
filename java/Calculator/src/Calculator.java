import operations.Divide;
import operations.Operation;
import operations.Subtract;
import operations.Multiply;
import operations.Sum;

import java.util.HashMap;
import java.util.Map;

public class Calculator {
    private Map<String, Operation> Operations;

    public Calculator() {
        Operations = new HashMap<>();
        Operations.put("1", new Sum());
        Operations.put("2", new Subtract());
        Operations.put("3", new Divide());
        Operations.put("4", new Multiply());

    }

    public double Calculate (String opcao, double a, double b){
        Operation Operation = Operations.get(opcao);
        return Operation.calculate(a,b);
    }
}
