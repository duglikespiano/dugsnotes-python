f = open('17_reading_multi_lines_data/text.txt', mode='r')
file_content = f.readlines()
file_content.append('Hello world hehehe\n')
file_content.append('Hello world hehehe\n')
file_content.append('Hello world hehehe\n')
file_content.append('Hello world hehehe\n')
file_content.append('Hello world hehehe\n')
f.close()


for line in file_content:
    print(line[:-1])
