# def sumDiff(x,y):
#     sum = x+y
#     diff = x-y
    
#     return sum,diff
# num1, num2 = eval(input("Enter two numbers(num1, num2):"))
# s, d = sumDiff(num1, num2)

# print("The sum is ",s,"and the difference is ",d)
# # result = sumDiff(5,5)
# # print(result)

# def addInterest(balance,rate):
#     newBalance = balance * (1 + rate)
#     return newBalance

# def test():
#     amount = 1000
#     rate = 0.05
#     amount = addInterest(amount, rate)
#     print(amount)
# test()


def addInterest(balances,rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1+rate)


def test():
    amounts = [1000,2200,800,360]
    rate = 0.05
    addInterest(amounts,0.05)
    print(amounts)
test()
