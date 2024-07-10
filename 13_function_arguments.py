def unlimited_arguments(*args, **keyword_args):
    print(args)
    print(keyword_args)
    for argument in args:
        print(argument)
    for key, argument in keyword_args.items():
        print(key, argument)


unlimited_arguments(*[1, 2, 3, 4], name='dug', age=20)
