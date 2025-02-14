import sys
import math
import random

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operation = sys.argv[3]
    result = None
    error = None
    
    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "mult":
        result = num1 * num2
    elif operation == "divi":
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

    if error_message:
        print(f"<p style='color:red;'>{error_message}</p>")
    else:
        print(f"<p>The result is: <strong>{operation}</strong></p>")
        print(f"<p>Input 1: <strong>{num1}</strong></p>")
        print(f"<p>Input 2: <strong>{num2}</strong></p>")
        print(f"<p>Result: <strong>{result}</strong></p>")
    
except ValueError:
    print("<h3>Error: Invalid input. Please provide two numbers and an operation.</h3>")
