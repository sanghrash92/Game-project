import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    times = 0
    print('You have 5 times to guess the num.')
    while guess != random_num:
        guess = int(input(f'Guess a number from 1 to {x}. '))
        if guess > random_num:
            print('Guess too high. Try again.')
        elif guess < random_num:
            print('Guess too low. Try again')
        else:
            print(f'Your guess is correct. The number was {random_num}.')
        times = times + 1
        if times >= 5:
            print('You didnt guess the number.')
            break 
            


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'The computer guessed it correctly. The number was {guess}.')
            

computer_guess(1000)   
        
    
