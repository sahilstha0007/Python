    # #Empty function
    # def greet():
    #     print('Hava a good day')

    # #call the function
    # greet()

    #Function with parameter

    # def greet(name):
    #     print("Hello",name)

    # #pass argument
    # greet("Suman")

    # # Functions with two arguments
    # def add_numbers(num1, num2):
    #     sum = num1 + num2
    #     print("Sum :",sum)
    # # Function call with two values
    # add_numbers(5,5)

    # # fuunction definition
    # def find_square(num):
    #     result = num * num
    #     return result

    # # function call
    # square = find_square(3)
    # print("Square: ",square)

    # Define functions for basic airthemetic operations
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():    
    while True:
        # Display the operation options
        print("Select operation:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")

        # Take input from the user for the operation
        choice = input("Enter choice (1/2/3/4/5):")
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        # creating if/else
        if choice in ['1','2','3','4']:
            # Take input from the user for the numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the chosen operation
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1,num2)}")
            
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1,num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1,num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                else:
                    print(f"{num1}/{num2} = {result}")

        else:
            print("Invalid input")
                
calculator()


