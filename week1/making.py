name =  input("Enter name:").title()
clas = input("Enter class:")
section = input("Enter section:")
eng = float(input("Enter English mark:"))
nep = float(input("Enter Nepali mark:"))
math = float(input("Enter Maths mark:"))
his = float(input("Enter History mark:"))
geo = float(input("Enter Geography mark:"))

# Calculating total marks and percentage
total_mark = eng + nep + math + his + geo
percentage = total_mark / 5

# Displaying the result
print("\n------Printing Result----------")
print("Name:", name)
print("Class:", clas)
print("Section:", section)
print("Percentage:", percentage, "%")

# Checking for errors and displaying remarks
if percentage < 0 or percentage > 100:
    print("Error: Percentage should be between 0 and 100 only!")
elif percentage < 45:
    print("Failed!")
else:
    print("Pass!")
    if 45 <= percentage < 60:
        print("Remark: Just Passed!")
    elif 60 <= percentage < 75:
        print("Remark: Good!")
    elif percentage >= 75:
        print("Remark: Excellent!")
