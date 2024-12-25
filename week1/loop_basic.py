# # Basic for loop 
# for i in "each word":
#     print(i)

# languages = ['swift','python','go']
# # acess elements of the list one by one
# for i in languages:
#     print(i)

# # Print Table using for loop
# def value(number):
#     # For loop
#     for i in range(1,11):
#         print(number,"x",i,"=",number*i)
# value(20)                 

# # loops in dictionary
# car = {"brand":"ford","model":"mustang","year":1964}
# for key in car.keys():
#     print(key,car[key])

# # Break for loop
# vehicles = ['Car','Cycle','Bus','Tempo']
# for v in vehicles:
#     if v == "Bus":
#         break
#     print(v)

# # continue in for loop
# vehicles = ['Car','Cycle','Bus','Tempo']
# for v in vehicles:
#     if v == "Bus":
#         continue
#     print(v) check it.....

# list_1 = ['Mango','Banana','Orange']
# list_2 = []
# for i in list_1:
#     list_2.append(i)
# print(list_2)

# finding maximum elements in a list
numbers = [1,4,50,800,12]
max = 0

for n in numbers:
    if(n>max):
        max = n
print(max)

''' WAP that prompts user for an amount of money in cents (of integer 'int') and express the 
    amount in number of 5o¢, 20¢, 10¢, 5¢ and 1¢. (Hint:use the operators // and %)'''

# Prompt the user for an amount in cents
amount = int(input("Enter the amount in cents: "))

# Calculate the number of 50¢ coins
fifty_cents = amount // 50
amount %= 50  # Update amount to the remainder

# Calculate the number of 20¢ coins
twenty_cents = amount // 20
amount %= 20

# Calculate the number of 10¢ coins
ten_cents = amount // 10
amount %= 10

# Calculate the number of 5¢ coins
five_cents = amount // 5
amount %= 5

# The remaining amount is in 1¢ coins
one_cent = amount

# Display the result
print(f"50¢ coins: {fifty_cents}")
print(f"20¢ coins: {twenty_cents}")
print(f"10¢ coins: {ten_cents}")
print(f"5¢ coins: {five_cents}")
print(f"1¢ coins: {one_cent}")
