

import random

print('Let me think of a Number between 1 to 80.')
level = input("Choose level of difficulty... Type 'easy' or 'hard': ").lower()

number = random.randint(1, 80)

def set_attempt():
    if level == 'easy':
        attempt = 10
    elif level == 'hard':
        attempt = 5
    else:
        print('Invalid Level selection!')
        attempt = 0
    return attempt

def guess_num(number, attempt):
    print(f'\nYou have {attempt} attempts remaining to guess the Number!')
    user_num = int(input('\nGuess the Number: '))
    if user_num < number:
        print('Your guess is Too Low')
    elif user_num > number:
        print('Your guess is Too High.')
    else:
        print(f'\nCongratulations!! You guessed the number {number} correct.')
        exit()
    if attempt > 1:
        print('Guess Again!')
    else:
        print('You are ou of Gueses. You Lose!')

attempt = set_attempt()
while attempt >= 1:
    if level == 'easy':
        guess_num(number, attempt)
        attempt -= 1
    else:
        guess_num(number, attempt)
        attempt -= 1