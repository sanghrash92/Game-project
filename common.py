filename = 'dracula.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()
    count_it = contents.count('Dracula')
    print(count_it)