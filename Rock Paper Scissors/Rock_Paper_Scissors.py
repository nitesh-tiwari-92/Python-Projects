

# Rock wins against Scissors
# Scissors wins against Paper
# Paper wins against Rock

from random import *

option = ['rock', 'paper', 'scissors']

def user_input(statement):
    user_ch = input(statement).lower()
    if user_ch in option:
        return user_ch
    else:
        print('Input Error. Please try again.')
        return user_input(statement)

retries = 10

while retries > 0:

    sys_ch = choice(option)
    user_ch = user_input('Enter rock, paper, or scissors: ')

    if user_ch == 'rock' and sys_ch == 'scissors':
        print(f'System Choice: {sys_ch} \nUser Selected: {user_ch}\nUser wins!\n')
    elif user_ch == 'scissors' and sys_ch == 'paper':
        print(f'System Choice: {sys_ch} \nUser Selected: {user_ch}\nUser wins!\n')
    elif user_ch == 'paper' and sys_ch == 'rock':
        print(f'System Choice: {sys_ch} \nUser Selected: {user_ch}\nUser wins!\n')
    elif user_ch == sys_ch:
        print(f'System Choice: {sys_ch} \nUser Selected: {user_ch}\nIt\'s a tie!\n')
    else:
        print(f'System Choice: {sys_ch} \nUser Selected: {user_ch}\nSystem Wins!\n')

    retries -= 1
