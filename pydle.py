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

def guess(round): # Player guesses word
    player_guess = ''

    while player_guess not in als: # Checks if guess is valid
        player_guess = input(f'Guess {round}: ', end="\r")
        if player_guess not in als:
            print('Guess not allowed', end="\r")
    
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
    print(hint)

als = word_reader('allowed-guesses.txt') # Generates possible answers set
solutions = list(word_reader('solutions.txt')) # Generates possible solutions list