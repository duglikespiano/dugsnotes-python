# Function
def my_function():
    print('hello world!')


my_function()


# *Args
def add_all(*numbers):
    result = 0
    for i in numbers:
        result += i
    print(result)


add_all(1, 2, 3, 4, 6, 7)


# **kwargs
def personal_information(nationality='Bikini Bottom', **personal_information):
    print(f'My name is {personal_information["name"]}')
    print(f'I am {personal_information["age"]} years old')
    print(f'I am from {nationality}')


personal_information(age=2, name='Patrick')
