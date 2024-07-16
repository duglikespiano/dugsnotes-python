def open_data():
    try:
        with open('text.txt', mode='w') as f:
            print(f)
    except IOError:
        print('doremi')
