from contextlib import nullcontext
import numbers
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.streak = 0

def word_reader(filename): # Reads a text file and generates set containing its words
    with open(filename) as dictfile:
        dic = set(w.upper() for w in dictfile.read().split('\n'))
    
    return dic

def new_word(): # Returns word from answer list
    word = random.choice(solutions)
    return word.upper()

def guess(tries): # Player guesses word
    player_guess = ''

    while player_guess not in als: # Checks if guess is valid
        player_guess = input(f'\nGuess #{tries}: ').upper()
        if player_guess not in als:
            print('\nGuess not allowed\n')
    
    return player_guess

def check_guess(guess, sol):
    hint = ''
    for i in range(len(guess)):
        if guess[i] == sol[i]:
            hint += f'{chr(10004)} ' # checkmark for correctly positioned letters
        elif guess[i] in sol:
            hint += f'{chr(10033)} ' # asterisk for letters in wrong position
        else:
            hint += f'{chr(10006)} ' # x for letters not in the word
    print(f'\t  {hint}\n')

def win_message(tries): # Prints win message depending on number of guesses it took to find word
    if tries == 6:
        print(f'Phew.')
    elif tries == 5:
        print('Great.')
    elif tries == 4:
        print('Splendid.')
    elif tries == 3:
        print('Impressive.')
    elif tries == 2:
        print('Magnificent.')
    else:
        print('Genius.')

def play_game(): # Simulates round of wordle
    solution = new_word()
    print('Guess the 5 letter word!')
    guess_number = 1

    while guess_number < 7:
        word = guess(guess_number)
        check_guess(word, solution)

        if word == solution:
            win_message(guess_number) # Player guessed correctly
            break
        
        guess_number += 1

    if guess_number == 7:
        print(f'You lost. The word was {solution}')

    
    

als = word_reader('allowed-guesses.txt') # Generates possible answers set
solutions = list(word_reader('solutions.txt')) # Generates possible solutions list
play_game()