import os
import webbrowser
from connect4 import connect4_main
from hangman1 import hangman_main
from tic_tac_toe_2 import tic_tac_toe_2_main
from tic_tac_toe_1 import tic_tac_toe_1_main
from profile_insert import profile_insert_main
from profile_pass import profile_pass_main

print('Hello, Welcome to this Gaming Interface.')

while True:
    print('''
1. New User
2. Existing User
''')
    user_login_choice = int(input('Which option do you choose? '))
    if user_login_choice == 1:
        profile_insert_main()
        print()
        if profile_pass_main():
            break
    elif user_login_choice == 2:
        if profile_pass_main():
            break

while True:
    print('''

What would you like to play?

1.Connect 4
2.Hangman
3.Tic Tac Toe (1 Player and 2 Player)
4.Quit (Exit the interface)
    ''')

    user_input = input('Which option do you choose: ')
    os.system('cls')

    if user_input == '1':
        ask = input('Do you want the rules ?(yes or no) ')
        if ask == 'yes':
            webbrowser.open("https://www.gamesver.com/the-rules-of-connect-4-according-to-m-bradley-hasbro/")
        connect4_main()
    elif user_input == '2':
        ask = input('Do you want the rules ?(yes or no) ')
        if ask == 'yes':
            webbrowser.open("https://www.wikihow.com/Play-Hangman")
        hangman_main()
    elif user_input == '3':
        ask = input('Do you want the rules ?(yes or no) ')
        if ask == 'yes':
            webbrowser.open("https://www.exploratorium.edu/brain_explorer/tictactoe.html")
        tictactoe_input = input('How many players, 1 or 2 ? ')
        if tictactoe_input == '1':
            tic_tac_toe_1_main()
        else:
            tic_tac_toe_2_main()
    else:
        print('Thank You for playing.')
        break




