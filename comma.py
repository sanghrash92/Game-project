# def listVal(spam):
#     spam.insert(-1, 'and')
#     print(spam)

# x = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'fox']
# listVal(x)
    
import random
numberOfStreaks = 0
coins = []
streak = 0
for experimentNumber in range(100):
   
    coins.append(random.randint(0, 1))
#     if flip == 0:
# #        print('Its heads.')
#         coins.append(flip)
#         heads += 1
        
#     else:
# #        print('its tails')
#         coins.append(flip)
#         tails += 1
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(coins)):
        if coins[i] == coins[i-1]:  #checks if current list item is the same as before
            streak += 1 
            
        else:
            streak = 0
            
        if streak == 6:
            numberOfStreaks += 1
        
print('Chance of streak: %s%%' % (numberOfStreaks / 100))