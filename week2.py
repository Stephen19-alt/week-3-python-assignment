# Creating an empty list called my_list
my_list = []

#Appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting 15 at the second position
my_list.insert(2, 15)

#Extending my_list with another list
my_list.extend([50, 60, 70])

#Removing the last element from my list
my_list.pop(-1)

#Sorting my list in ascending order
my_list.sort()

#Finding and printing index of 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30 is:", index_of_30)



