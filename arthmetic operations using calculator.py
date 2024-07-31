import calculator

def main():

 try:

    num1 = float(int(input("enter the number one ")))
    num2 = float(int(input("enter the number two ")))
    operation = input("enter the arthemetic operator ")

    if operation == '+':
       result=calculator.sum(num1, num2)
    elif operation == '-':
       result=calculator.subtract(num1, num2)
    elif operation == '*':
        result=calculator.multiplication(num1, num2)
    elif operation == '/':
        result=calculator.division(num1, num2)
    else:
        raise ValueError("Invalid operator")

    print(f"result of {num1} {operation} {num2} is {result}")


 except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
   main()



