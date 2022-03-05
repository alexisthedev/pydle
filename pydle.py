import random

class Game:
    def __init__(self):
        self.solutions = list(word_reader('solutions.txt')) # Generates possible solutions list
        self.allowed = word_reader('allowed-guesses.txt') # Generates valid answers set
        self.mystery_word = random.choice(self.solutions)
        self.player_guesses = [' '*5, ' '*5, ' '*5, ' '*5, ' '*5, ' '*5]
        self.hints = [' '*5, ' '*5, ' '*5, ' '*5, ' '*5, ' '*5]
    
    def new_round(self): # Returns word from answer list
        self.mystery_word = random.choice(self.solutions)
        self.player_guesses = [' '*5, ' '*5, ' '*5, ' '*5, ' '*5, ' '*5]
        self.hints = [' '*5, ' '*5, ' '*5, ' '*5, ' '*5, ' '*5]
    
    def make_board(self):
        """
        Creates an empty game board (visualization)
        """

        board = [[] for x in range(6)]

        for i in range(6):
            round_no = i+1 # Number of guess at the start of row
            board[i].append(f'{round_no}|')
            for j in range(5): # Adds the cells to each row
                board[i].append(f'   {self.player_guesses[i][j]}|')
            # board[i].append(f'   {self.hints[i]}')

        board.insert(0, '-'*30) # First row of ---
        board.append('-'*30) # Last row of ---

        return board
    
    def guess(self, tries):
        word = ''
        while word not in self.allowed:
            word = input().upper()
            if word not in self.allowed:
                print('Guess not valid')
        self.player_guesses[tries] = word
    
    def check_guess(self, player_guess):
        hint = ''
        for i in range(len(player_guess)):
            if player_guess[i] == self.mystery_word[i]:
                hint += f'{chr(10004)} ' # Letter in correct spot (checkmark)
            elif player_guess[i] in self.mystery_word:
                hint += f'{chr(10033)} ' # Letter is in word (asterisk)
            else:
                hint += f'{chr(10006)} ' # Letter is not in word (x)
        
        tries = 6
        for i in range(6):
            if self.player_guesses[i] == '     ':
                tries = i-1
        self.hints[tries] = hint
    
    def win_message(self): # Prints win message depending on number of guesses it took to find word
        tries = 7
        for i in range(6):
            if self.player_guesses[i] == '     ':
                tries = i

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
        elif tries == 1:
            print('Genius.')
        else:
            print(f'You lost. The word was {self.mystery_word}')
    
    def play_game(self): # Simulates round of wordle
        self.new_round()
        print('Guess the 5 letter word!')
        guess_number = 1

        for i in range(6):
            self.guess(i)
            self.check_guess(self.player_guesses[i])
            print_board(self.make_board())
        
        self.win_message()

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.streak = 0

def word_reader(filename): # Reads a text file and generates set containing its words
    with open(filename) as dictfile:
        dic = set(w.upper() for w in dictfile.read().split('\n'))
    
    return dic

def print_board(board):
    for line in board:
        print(''.join(line))

wordle = Game()
wordle.play_game()