my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Sliced List (1:3):", my_list[1:3])

my_list.append(60)    #add         
print("After append:", my_list)

my_list.insert(2, 25)         
print("After insert:", my_list)

my_list.extend([70, 80])
print("After extend:", my_list)

my_list.remove(25)             
print("After remove:", my_list)
#
popped = my_list.pop(2)          
print("After pop:", my_list)
print("Popped element:", popped)

my_list[0] = 100
print("After updating index 0:", my_list)

print("Length of list:", len(my_list))

print("Is 30 in list?", 30 in my_list)

my_list.sort()
print("Sorted List:", my_list)

my_list.reverse()
print("Reversed List:", my_list)

print("Count of 40:", my_list.count(40))

if 40 in my_list:
    print("Index of 40:", my_list.index(40))

nested = [[1, 2], [3, 4], [5, 6]]
print("Nested List:", nested)
print("Access nested element:", nested[1][0])
