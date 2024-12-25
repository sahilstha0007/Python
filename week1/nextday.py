# name =  input("Enter name:").title()
# clas = input("Enter class:")
# section = input("Enter section:")
# eng = float(input("Enter English mark:"))
# nep = float(input("Enter Nepali mark:"))
# math = float(input("Enter Maths mark:"))
# his = float(input("Enter History mark:"))
# geo = float(input("Enter Geography mark:"))

# total_mark = eng + nep + math + his + geo
# percentage = total_mark/5

# print("\n------Printing Result----------")
# print("Name",name)
# print("Class",clas)
# print("Section",section)
# print("Percentage",percentage,"%")
# if percentage <0 or percentage >100:
#     print("Error: Percentage should be between 0 and 100 only!")
# elif percentage <45:
#     print("Failed!")
# elif percentage >=45:
#     print("Pass!")
#     if percentage >=45 and percentage<60:
#         print("Remark: Just Passed!")
#     elif percentage >=60 and percentage<75:
#         print("Remark: Good!")

#Prompt the user for input
#getting output in ---hours---min--sec

time_in_seconds = int(input("Enter a time in seconds:"))

#calculate hours,minutes and seconds
hours = time_in_seconds // 3600
remaining_seconds = time_in_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Displaying the result
print(f"{time_in_seconds} seconds = {hours} hours {minutes} minutes {seconds} seconds")