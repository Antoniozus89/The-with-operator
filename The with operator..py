file_name = 'Homework.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    content = file.read()
    print(content)