# String
my_string = 'hello'
my_string = my_string + 'world'

# Number
my_number = 1
my_number = my_number + 3

# Boolean
my_boolean = True
my_boolean = False

# List
my_list = [1]
my_list.append('123')  # type: ignore

# Tuple
my_tuple = (1, 2, 3)
# tuple can not be edited

# Dictionary
my_dictionary = {'name': 'dug', 'age': 20}

# Set
my_set = set([1, 2, 3, 1, 2, 3])


print(f'This is my string {my_string}')
print(f'This is my number {my_number}')
print(f'This is my boolean {my_boolean}')
print(f'This is my list {my_list}')
print(f'This is my tuple {my_tuple}')
print(f'This is my dictionary {my_dictionary}')
print(f'This is my set {my_set}')
