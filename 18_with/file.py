with open('18_with/text.txt', mode='w+') as f:
    file_content = f.readlines()
    file_content.append('Hello world hehehe\n')
    file_content.append('Hello world hehehe\n')
    file_content.append('Hello world hehehe\n')
    file_content.append('Hello world hehehe\n')
    file_content.append('Hello world hehehe\n')
    f.write('doremi')
    for line in file_content:
        print(line[:-1])
