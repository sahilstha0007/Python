# def items()


item1 = int(input("Enter the cost of the 1st item"))
item2 = int(input("Enter the cost of the 2nd item"))
item3 = int(input("Enter the cost of the 3rd item"))

costof3item= item1 +item2 +item3

discount = costof3item *0.1
Netcost = costof3item - discount
print(f"The net cost of 3 items are {Netcost}")