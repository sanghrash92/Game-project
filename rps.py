import random
import sys


ties = 0
win = 0
loss = 0
total_game = 10

print("Let's play a game of rock, paper and scissor!")
plays = 'rock', 'paper', 'scissor'
comp = random.choice(plays)

while total_game > 0:
    player = input("rock, paper or scissor or 'q' to quit? \n")
    if player == 'q':
        sys.exit()
    if player == comp:
        print('It\'s a tie!')
        ties += 1
        total_game -= 1
        
    elif player == 'rock' and comp == 'scissor':
        print("You win!")
        win += 1
        total_game -= 1
    elif comp == 'rock' and player == 'scissor':
        print('You lose!')
        loss += 1
        total_game -= 1
    elif player == 'paper' and comp == 'rock':
        print("You win!")
        win += 1
        total_game -= 1
    elif comp == 'paper' and player == 'rock':
        print('You lose!')
        loss += 1
        total_game -= 1
    elif player == 'scissor' and comp == 'paper':
        print('You win!')
        win += 1
        total_game -= 1
    elif comp == 'scissor' and player == 'paper':
        print('You lose!')
        loss += 1
        total_game -= 1
    print(total_game)
    
print('wins: ', win)
print('loss: ', loss)
print('ties: ', ties)