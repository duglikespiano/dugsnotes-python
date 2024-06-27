# list comprehension
simple_list = [1, 2, 3, 4]
doubled_list = []

for element in simple_list:
    doubled_list.append(element*2)
print(doubled_list)

doubled_list = []
print(doubled_list)

doubled_list = [element*2 for element in simple_list]
print(doubled_list)


doubled_list = [element*2 for element in simple_list if element % 2 == 0]
print(doubled_list)
