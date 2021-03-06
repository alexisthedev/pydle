import random
import os

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
            elif player_guess[i] in letters:
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
            print(f'\t\t  You lost. The word was {self.mystery_word}\n\n')
    
    def play_game(self): # Simulates round of wordle
        print('\t\t  Guess the 5 letter word!')

        for i in range(6):
            self.guess()
            self.check_guess(self.player_guesses[i])
            print('\n\n')
            clear()
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

def word_reader(filename): # Reads a text file and generates set containing its words
    with open(filename) as dictfile:
        dic = set(w.upper() for w in dictfile.read().split('\n'))
    
    return dic

clear = lambda: os.system('cls') # Clears the command line

game = Game()
testboard = Board()
testboard.add_word('WEARY', f'{chr(10004)} {chr(10033)} {chr(10033)} {chr(10033)} {chr(10006)} ')

# <-- Changes Font. Credit to Marfisa on stackoverflow.com-->

import ctypes

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 11
font.dwFontSize.Y = 18
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "SimSun-ExtB"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))


# <--- Introduction Message & Game Rules --->
clear()
print('\n\n\t\t[PYDLE]')
print('\nWelcome to Pydle! A Wordle clone in python!\n')
print('\t\t[RULES]\n')
print('Guess the mystery 5 letter word in at most 6 guesses!')
print('For each letter in your guess, get a character hinting at information on its respective letter:')
print(f' - {chr(10004)} means that the letter is in the correct spot.')
print(f' - {chr(10033)} means that the letter is in the word, but in another position.')
print(f' - {chr(10006)} means that the letter is not in the word.')
print(f'For example, if the mystery word was WATER then a guess of WEARY would return these hints\n\n')
testboard.print_board()
input('\n\nAre you ready? Enter anything to continue.')
clear()

# <--- Actual Game --->
while True:
    game.play_game()
    ans = input('Enter any input to play again, enter "N" to exit.\n\n').upper()
    clear()
    if ans == 'N':
        break
    game.new_round()