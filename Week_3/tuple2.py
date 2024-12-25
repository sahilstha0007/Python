# Working with tuples
my_tuple = (10,20,30,40,50)

second_element = my_tuple[1]
print("Second element:",second_element)
# my_tuple.append(70)

temp_list = list(my_tuple)
temp_list.append(60)
my_tuple = tuple(temp_list)
print("New tuple:",my_tuple)
