# while True:
#     print('Enter your age: ')
#     age = input()
#     try:
#         age = int(age)
#     except:
#         print('Please use numueric digits.')
#         continue
        
#     if age < 1:
#         print('Please enter a positive number.')
#         continue
        
#     break
    
# print(f'Your age is {age}.')

# Idiot.py

import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours? \n'
    response = pyip.inputYesNo(prompt)
    
    if response == 'no':
        break
        print('Thank you. Have a nice day.')
    