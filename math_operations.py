import sys
import math
import random

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operation = sys.argv[3]
    result = None
    error = None
    
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            error = "Error: Division by zero is not allowed."


    if result is not None:
        if result > 100:
            result *= 2
        elif result < 0:
            result += 50
            
    print("<h3>Result</h3>")

    if error:
        print(f"<p style='color:red;'>{error}</p>")
    else:
        print(f"<p>The result is: <strong>{operation}</strong></p>")
        print(f"<p>Input 1: <strong>{num1}</strong></p>")
        print(f"<p>Input 2: <strong>{num2}</strong></p>")
        print(f"<p>Result: <strong>{result}</strong></p>")
    
except ValueError:
    print("<h3>Error: Invalid input. Please provide two numbers and an operation.</h3>")
