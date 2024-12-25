# Finding discount and deducting
item_1 = float(input("Enter the price of first item:"))
item_2 = float(input("Enter the price of second item:"))
item_3 = float(input("Enter the price of third item:"))

# Calculating total cost
total_cost = item_1 + item_2 + item_3

#calculating discount
discount = (10/100) * total_cost

#calculating net cost after discount
Net_cost = total_cost - discount

# # Displaying
# print(f"Total cost:{total_cost}")
# print(f"Discount:{discount}")
# print(f"Net cost:{Net_cost}")

# Another method
print("Cost of 3 items = RM{:.2f}".format(total_cost))
print("10% discount = RM{:.3f}".format(discount))
print("Net cost = RM{:3f}".format(Net_cost))    