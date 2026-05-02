
import random

print('\nLet\'s play Hangman!!\n')
print('''You have only 6 lives/ attempts, try to guess the correct word/ letter\'s within 6 attempts!\n
Good Luck!!\n''')

words = ['Apple', 'Ball', 'Cat', 'Dog', 'Elephant', 'Fish', 'Goat', 'House', 'Ice', 'Jungle', 'Kite', 'Lion', 'Monkey', 'Nest', 'Orange', 'Parrot', 'Queen', 'River', 
         'Sun', 'Tiger', 'Umbrella', 'Van', 'Water', 'Xylophone', 'Yak', 'Zebra', 'Book', 'Chair', 'Table', 'Window', 'Door', 'Road', 'Tree', 'Flower', 'Grass']

rand_word = (random.choice(words)).lower()

word = []

for i in range(len(rand_word)):
    word.append('_')

print(word)

attempt = 6

while attempt >= 1:

    guess_wrd = input('\nGuess the letter\'s: ').lower()

    if guess_wrd not in rand_word:
        print(f'\nYou guessed {guess_wrd} that is not present in the word. So you lose a life/ attempt.\n')
        attempt -= 1
        print(f'Remainng attempt: {attempt}')

    else:
        new_word = ''

        for i in range(len(rand_word)):

            if guess_wrd == rand_word[i]:
                word[i] = guess_wrd

        print(word)

        for w in word:
            new_word += w

        if new_word == rand_word:
            break


if new_word == rand_word:
    print(f'\nYou Won! Congratulations! for guessing the correct word {new_word}.\n')
else:
    print('\nYou lose! Please try again later.\n')
