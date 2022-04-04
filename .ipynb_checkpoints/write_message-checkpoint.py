filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
    while True:
        ask = input("What's your name?")
        if ask == 'Quit'.lower():
            break
        print(f"Hello {ask}! Nice to meet you!")
        file_object.write(f"{ask}\n")