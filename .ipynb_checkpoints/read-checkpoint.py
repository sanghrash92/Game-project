
def animal_name(filename):
    try: 
        with open(filename) as f:
            contents = f.read()
            
    except FileNotFoundError:
        pass
    else:
        print(contents)
files = ['cats.txt', 'dogs.txt', 'animal.txt']
for file in files:
    animal_name(file)