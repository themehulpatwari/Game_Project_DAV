import random
import os
from word import word_list

# Prints the figure
def print_scaffold(guesses):
    if guesses == 6:
        print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """)
    elif guesses == 5:
        print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """)
    elif guesses == 4:
        print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """)
    elif guesses == 3:
        print("""
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """)
    elif guesses == 2:
        print("""
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """)
    elif guesses == 1:
        print("""
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """)
    elif guesses == 0:
        print("""
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """)

def valid(user_choice, user_letter):
    if len(user_choice) == 1:
        alpha_compare = ord(user_choice)
        if (97 >= alpha_compare >= 122) or (65 >= alpha_compare >= 90):
        # Checking whether input is between a to z
            print('Invalid, please try again.')
            return False
        elif user_choice in user_letter:
            print('This letter has already been guessed')
            return False
        else:
            return True
    else:
        print('Invalid, please try again.')
        return False

def hangman_main():
    win = 0
    lose = 0
    game_input = 'yes'
    while game_input == 'yes':
        guess = 0
        chance = 0
        word = random.choice(word_list)
        # Chooses a word at random
        list2 = []
        user_letter = []
        for i in word:
            list2.append('_')
            # Appends the list with '_' ; for example: word = 'hi', list2 = ['_','_']
        print('\nYou only have 7 chance')
        print('\nNo of letters in the word =',len(word))

        while guess<6:
            num_index = 0
            print_scaffold(guess)
            print('\nAlready Guessed Words =',user_letter,'\n')
            while True:
                user_choice = input('What is your guess? ')
                if valid(user_choice, user_letter):
                    chance += 1
                    break
            user_letter.append(user_choice)
            os.system('cls')

            if not (user_choice in word):
                guess += 1

            for i in word:
            # Iterates over the word to check whether user has given a letter present in the random word chosen
                if user_choice == i:
                    list2[num_index] = i
                    # If the letter is present in the word then the value of '_' is changed with the letter
                else:
                    pass
                num_index += 1
            print(' '.join(list2))
            # Prints the correct letter guessed along with blanks.
            if word == (''.join(list2)):
                print('You guessed the word in {} tries'.format(chance))
                win += 1
                break
        else:
            print('\nSorry you lose, the word was', word)
            lose += 1
        game_input = input('\n\nPlease reply with only yes or no \nDo you want to play Hangman again? ')

    print('\nTotal Games Played = {}\nGames Won = {}\nGames Lost = {}'.format(win + lose,win,lose))

if __name__ == '__main__':
    hangman_main()
