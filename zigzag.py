import time, sys

# indent = 0
# indentIncreasing = True

# try:
#     while True:
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(1)
        
#         if indentIncreasing:
#             indent = indent + 1
#             if indent == 20:
#                 indentIncreasing = False
                
#         else:
#             indent = indent - 1
#             if indent == 0:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
            time.sleep(0.5)
            
        elif number % 2 == 1:
            number = number * 3 +1
            print(number)
try:            
    val = int(input('write any num: '))
    collatz(val)
except:
    print('Please write a valid number')
    

# import time            
# x = 45
# while x != 1:
#     if x % 2 == 0:
#         x = x // 2
#         print(x)
#         time.sleep(1)
#     elif x % 2 == 1:
#         x = x * 3 + 1
#         print(x)
        