while True:
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    
    c = input("Enter the operation (+, -, *, /) or type 'exit' to quit: ")
    
    if c.lower() == 'exit':
        print("Exiting the program.")
        break
    
    if c == '+':
        d = a + b
        print(d)
    elif c == '-':
        e = a - b
        print(e)
    elif c == '*':
        f = a * b
        print(f)
    elif c == '/':
        if b != 0:
            g = a / b
            print(g)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")
