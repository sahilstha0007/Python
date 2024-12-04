#Creating a list
int_list = list(range(1,11))
#Display list
print( "list of integers", int_list)

#modifying list
repeated_list = int_list * 2

#printing item in the list
for item in int_list:
    print(item)

third_element = int_list[2]
print("3rd element:", third_element)


last_element = int_list[-1]
print("last element:", last_element)


#slicing  the list
slice_list = int_list[2:6]
print("Slice form index2 to 5:",slice_list)

last_three_element = int_list[-3:]
print("Last three elements:", last_three_element)

#Using list methods
int_list.append(11)
print("After inserting 50 at the beginning", int_list)

int_list.insert(0,50)
print("After inserting 50 at the beginning:", int_list)

int_list.remove(5)
print("After  removing 5:",int_list)

int_list.sort()
print("After sorting:", int_list)

int_list.reverse()
print("After reversing:",int_list)

square_list =[x**2 for x in int_list]
print("List of square:", square_list)


even_list = {x for x in int_list}
print("List of even number", even_list)


matrix = [
    [1,2,3],
    {4,5,6},
    [7,8,9]
]

element= matrix[1,2]
print("Elements in seconds row,third column", element)
print("Matrix")
for row in matrix:
    print(row)