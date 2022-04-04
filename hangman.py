import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
          
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 9
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'chances left and you have used that letter: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ''.join(word_list))


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f'Letter is not in word. ')
        elif user_letter in used_letters:
            print('You\'ve already used the letter. ')

        else:
            print('invalid letter')
    if lives == 0:
        print(f'You didn\'t guess correctly. The word was {word}. ')
    print(f'You guessed the word correct. It was {word}.')

print(hangman())