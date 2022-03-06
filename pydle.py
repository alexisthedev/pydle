import random

class Game:
    def __init__(self):
        self.solutions = list(word_reader('solutions.txt')) # Generates possible solutions list
        self.allowed = word_reader('allowed-guesses.txt') # Generates valid answers set
        self.mystery_word = random.choice(self.solutions)
        self.player_guesses = [' '*5, ' '*5, ' '*5, ' '*5, ' '*5, ' '*5]
        self.hints = [' '*5, ' '*5, ' '*5, ' '*5, ' '*5, ' '*5]
        self.wrong_letters = []
        self.tries = 0
        self.board = Board()
    
    def new_round(self): # Returns word from answer list
        self.mystery_word = random.choice(self.solutions)
        self.player_guesses = [' '*5, ' '*5, ' '*5, ' '*5, ' '*5, ' '*5]
        self.hints = [' '*5, ' '*5, ' '*5, ' '*5, ' '*5, ' '*5]
        self.wrong_letters = []
        self.tries = 0
        self.board = Board()
    
    def guess(self):
        word = ''
        while word not in self.allowed:
            word = input().upper()
            if word not in self.allowed:
                print('Guess not valid')
        self.player_guesses[self.tries] = word
    
    def check_guess(self, player_guess):
        letters = list(self.mystery_word)
        hint = ''
        for i in range(len(player_guess)):
            if player_guess[i] == self.mystery_word[i] and player_guess[i] in letters:
                hint += f'{chr(10004)} ' # Letter in correct spot (checkmark)
                letters.remove(player_guess[i])
            elif player_guess[i] in self.mystery_word and player_guess[i] in letters:
                hint += f'{chr(10033)} ' # Letter is in word (asterisk)
                letters.remove(player_guess[i])
            else:
                hint += f'{chr(10006)} ' # Letter is not in word (x)
                if player_guess[i] not in self.wrong_letters and player_guess[i] not in self.mystery_word:
                    self.wrong_letters.append(player_guess[i])
                    self.wrong_letters.sort()
        
        self.hints[self.tries] = hint
        self.board.add_word(player_guess, hint)
    
    def win_message(self): # Prints win message depending on number of guesses it took to find word
        if self.tries == 5:
            print('\t\t  Phew.')
        elif self.tries == 4:
            print('\t\t  Great.')
        elif self.tries == 3:
            print('\t\t  Splendid.')
        elif self.tries == 2:
            print('\t\t  Impressive.')
        elif self.tries == 1:
            print('\t\t  Magnificent.')
        elif self.tries == 0:
            print('\t\t  Genius.')
        else:
            print(f'\t\t  You lost. The word was {self.mystery_word}')
    
    def play_game(self): # Simulates round of wordle
        print('\t\t  Guess the 5 letter word!')

        for i in range(6):
            self.guess()
            self.check_guess(self.player_guesses[i])
            print('\n\n')
            self.board.print_board()
            print(f'\t\t Letters not in word: {self.wrong_letters}')

            if self.player_guesses[self.tries] == self.mystery_word:
                break
            
            self.tries += 1
        
        self.win_message()

class Board:
    def __init__(self):
        self.board = [[], [], [], [], [], []]
        self.guesses = 0
    
    def add_word(self, word, hint):
        self.board[self.guesses].append('|')
        for i in range(5):
            self.board[self.guesses].append(f'  {word[i]}  |')
        self.board[self.guesses].append(f'\t [ {hint}]')
        self.guesses += 1
    
    def print_board(self):
        print('\t\t' + '-'*31)
        for i in range(self.guesses):
            print('\t\t' + ''.join(self.board[i]))
            print('\t\t' + '-'*31)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.streak = 0

def word_reader(filename): # Reads a text file and generates set containing its words
    with open(filename) as dictfile:
        dic = set(w.upper() for w in dictfile.read().split('\n'))
    
    return dic

game = Game()
game.play_game()