# Function to print the multiplication table of a given number
def multiplication_table(n):
    print(f"Multiplication table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Input: Asking the user to enter the number
n = int(input("Enter a number to calculate its multiplication table: "))

# Calling the function
multiplication_table(n)
