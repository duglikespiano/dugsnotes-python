# Conditionals
my_boolean = True
my_index = 0


def my_loop(index):
    while (my_boolean):
        global my_index
        my_index += 1

        if (my_index < 5):
            print(f'My index is {my_index} and smaller than 5')

        elif (my_index < index and my_index != 7):
            print(f'My index is {my_index} and smaller than {index}')

        elif (my_index < index and my_index == 7):
            continue
            print("This line won't be executed")

        else:
            print(f'My index reached {index}, program will be terminated')
            my_index = 0
            break


my_loop(10)
