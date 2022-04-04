# import random

# def play():
#     games = 10
#     while games:

#         user = input("'r' for roc(k, 'p' for paper, 's' for scissors.\n")
#         computer = random.choice(['r', 'p', 's'])

#         if user == computer:
#             return 'Tie!'
#         if win(user, computer):
#             return 'You win!'
#         return 'You lose!'
#         games = games - 1
#         if games <= 0:
#             break

# def win(player, opponent):
#     if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r')\
#     or (player == 's' and opponent == 'p'):
#         return False

# print(play())
import random
                              
def play():
    games = 10
    wins = 0
    loss = 0
    ties = 0
    
    while games > 0:
        print('%s Wins, %s Loss, %s Tie, %s Games' % (wins, loss, ties, games))
        user = input("'r' for rock, 'p' for paper, 's' for scissor!\n")
        computer = random.choice(['r', 'p', 's'])
        
        if computer == user:
            print('It\'s a tie')
            ties = ties + 1
        if losses(computer, user):
            print('You lose!')
            loss = loss + 1
             
        if win(user, computer):
            print('You win!')
            wins = wins + 1
            
        games = games - 1
        if games <= 0:
            break
            
        
def losses(opponent, player):
    if (opponent == 'r' and player == 's') or (opponent == 'p' and player == 'r')\
    or (opponent == 's' and player == 'p'):
        
       
        return True

def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r')\
    or (player == 's' and opponent == 'p'):
        
        return True

print(play())
        