simple_list = [1, 2, 3, 4]


def multiply(el):
    return el * 2


print(map(multiply, simple_list))
print(list(map(multiply, simple_list)))
print(list(map(str, simple_list)))
