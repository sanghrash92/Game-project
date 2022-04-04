arith = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "232 + 12"]
if len(arith) > 5:
    print('Error, too many problems.')
    
top = []
bottom = []
dashes = []
spaces = '    '
answers = []
    
for problems in arith:
    first = problems.split()[0]
    second = problems.split()[2]
    first_length = len(first)
    second_length = len(second)
    diff_first = first_length - second_length
    diff_second = second_length - first_length
    first_just = first.rjust(int(second_length))
    second_just = second.rjust(int(first_length))
    
    first_width = len(problems.split()[0])
    second_width = len(problems.split()[2])
    if first_width > 4 or second_width > 4:
        print("Error: Numbers cannot be more than four digits.")
    

    print(first, first_width, second[1], second_width)