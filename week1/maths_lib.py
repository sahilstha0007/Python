# import math

# def main():
#     print("This program finds the real solution to  a quadratic")
#     print()

#     a,b,c = eval(input("Please enter the coefficients(a,b,c):"))

#     discRoot = math.sqrt(b*b-4*a*c)
#     root1 = (-b + discRoot)/(2*a)
#     root2 = (-b - discRoot)/(2*a)

#     print()
#     print("The solutions are :",root1,root2)
    
# main()

# n = int(input("Enter no. to find factorial:"))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print("Factorial:",fact)


# Calculating future interest with initial amount

# def calculate_deposit_amount(future_value,annual_interest_rate,years):
#     deposit_amount = future_value / (1+annual_interest_rate) ** years
#     return deposit_amount

# # Example usage:
# future_value = 10000 #we want $10,000 in the account at the end of 10 years
# annual_interest_rate = 0.05
# years = 10 #We plan to let the money sit in the account for 10 years.

# deposit_amount = calculate_deposit_amount(future_value, annual_interest_rate, years)
# print(f"You need to deposit ${deposit_amount:.2f} today to achieve a future value of ${future_value}.")

# greet = "Hello Bob"
# # print(greet[0])
# print(greet[0],greet[2],greet[4])

# Indexing = 1 words && slicing = multiple words

# a = "reacting" 
# # print(a[7],a[0],a[1],a[2],a[4]) #printing great from reacting
# print(a[-1],a[0:3],a[4]) #slicing method

#  Giving month through user's number

def main():
    # months is used as as lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = eval(input("Enter a month under (1-12):"))

    # Compute starting position of month n in months
    pos = (n-1)*3

    # Grab the appropriate slice from months
    monthAbbrev = months[pos:pos + 3]

    # print the result
    print("The month abbreviation is ", monthAbbrev + ".")

main()