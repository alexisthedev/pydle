class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.streak = 0

def new_word(): # Returns word from answer list (online)
    word = 'CRANE'
    return word.capitalize()

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

def play_game():
    word = new_word()
    print('Guess the word!')
    for i in range(6):
        print(f'Guess {i+1}')
        check_guess(input().capitalize(), word)

play_game()