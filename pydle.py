import random

class Game:
    def __init__(self):
        self.solutions = list(word_reader('solutions.txt')) # Generates possible solutions list
        self.allowed = word_reader('allowed-guesses.txt') # Generates valid answers set
        self.mystery_word = random.choice(self.solutions)
        self.player_guesses = []
    
    def new_round(self): # Returns word from answer list
        self.mystery_word = random.choice(self.solutions)
        self.player_guesses = []
    
    def guess(self):
        word = ''
        while word not in self.allowed:
            word = input().upper()
            if word not in self.allowed:
                print('Guess not valid')
        self.player_guesses.append(word)
    
    def check_guess(self, player_guess):
        hint = ''
        for i in range(len(player_guess)):
            if player_guess[i] == self.mystery_word[i]:
                hint += chr(10004) # Letter in correct spot (checkmark)
            elif player_guess[i] in self.mystery_word:
                hint += chr(10033) # Letter is in word (asterisk)
            else:
                hint += chr(10006) # Letter is not in word (x)
        
        return hint
    
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
    
    def play_game(self): # Simulates round of wordle
        self.new_round()
        print('Guess the 5 letter word!')
        guess_number = 1

        while guess_number < 7:
            self.guess()
            word = self.player_guesses[-1]
            hint = self.check_guess(word)
            print(hint)

            if self.player_guesses[-1] == self.mystery_word:
                self.win_message(guess_number) # Player guessed correctly
                break
            
            guess_number += 1

        if guess_number == 7:
            print(f'You lost. The word was {self.mystery_word}')

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.streak = 0

def word_reader(filename): # Reads a text file and generates set containing its words
    with open(filename) as dictfile:
        dic = set(w.upper() for w in dictfile.read().split('\n'))
    
    return dic

        


wordle = Game()
wordle.play_game()