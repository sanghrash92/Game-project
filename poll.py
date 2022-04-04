filename = 'polling.txt'

with open(filename, 'a') as file_object:
    while True:
        reason = input("Why do you like programming? ")
        if reason == 'No'.lower():
            break
        file_object.write(f"{reason}\n")
        