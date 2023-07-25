from GuessGame import play as play_guess_game
from MemoryGame import play as play_memory_game
from CurrencyRouletteGame import play as play_currency_roulette_game
from Score.Score import add_score


def welcome():
    name = input('Please enter your name: ')
    output = f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.'
    return output


def choose_difficulty():
    difficulty = input('Please choose game difficulty from 1 to 5:')
    if not difficulty.isdigit():
        print('You have entered a wrong value.')
        return choose_difficulty()
    elif int(difficulty) not in range(1, 6):
        print('Game difficulty not in allowed range.')
        return choose_difficulty()
    else:
        print(f'You have chosen difficulty {difficulty}.')
        return int(difficulty)


def load_game():
    while True:
        game = input('''Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        ''')
        if not game.isdigit():
            print('You have entered a wrong value.')
        elif int(game) not in range(1, 4):
            print('Game number not in allowed range.')
        else:
            print(f'You have chosen game number {game}.')
            difficulty_level = choose_difficulty()
            if int(game) == 1:
                score = play_memory_game(difficulty_level)
                if score:
                    add_score(difficulty_level)
            elif int(game) == 2:
                score = play_guess_game(difficulty_level)
                if score:
                    add_score(difficulty_level)
            elif int(game) == 3:
                score = play_currency_roulette_game(difficulty_level)
                if score:
                    add_score(difficulty_level)

        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() != 'yes':
            break



