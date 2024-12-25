### Imp VVIC*******************************************

class Subject:
    def __init__(self, name , code, credits): 
        self.name = name
        self.code = code
        self.credits = credits
    
    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_code(self):
        return self.code

    def set_code(self,code):
        self.code = code

    def get_credits(self):
        return self.credits
        
    def set_credits(self, credits):
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.code}) with {self.credits} credits"


# Example usage:
subject1 = Subject("Discrete Mathematics", "BIT108", 4)
print(subject1) # Output: Discrete Mathematics 

print(subject1.get_name())
subject1.set_name("Calculus")
print(subject1.get_name()) #Output: Calculus

subjectList = [] #initialize an empty list to store Subject objects

#Open the file for reading
with open('subjectData.txt',"r") as file:
    #Read each line from the file
    for line in file:
        #Split the line by comma to extract name, code, and credits
        data = line.strip().split(',')
        subject = Subject(data[0], data[1], int(data[2]))
        #Append the Subject object to the subjectList
        subjectList.append(subject)
print(subjectList)
#Now subjectList contains all Subject objects read from the file

for subject in subjectList:
    print(subject)

#Create a new Subject object
new_subject = Subject("Final Year Project II","BIT305",5)

#Add the new subject to the subjectList
subjectList.append(new_subject)

#Initialize a counter for Year 3 subjects
year_3_count=0

# Iterate through each subject in subjectList
for subject in subjectList:
    # Check if the subject code indicates it's a Year 3 subject (code ends with "3")
    if subject.get_code()[3] == "3":
        year_3_count +=1

# Display the number of Year 3 subjects 
print("Number of Year 3 subjects:", year_3_count)

# Calculate the total credits and count of subjects
total_credits = 0
num_subjects = len(subjectList)

#Iterate through each subject in subjectList
for subject in subjectList:
    #Add the credits of the current subject to the total
    total_credits += subject.get_credits()
#Calculate the average credit
average_credit = total_credits / num_subjects

#Display the average credit
print("Average credit of all subject:", average_credit)

#open the file for writing 
with open("newSubjectData.txt",'w') as file:
    #Iterate through each subject in subjectList
    for subject in subjectList:
        #Write the details of the subject as a line in the file
        file.write(f"{subject.get_name()}, {subject.get_code()}, {subject.get_credit()}")