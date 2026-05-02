

import dataset
import random
import os


def user_response():
    while True:
        user_input = input("\nWho has more followers? Type '1' or '2': ").strip()
        if user_input in ['1', '2']:
            user_input = int(user_input)
            return user_input
        print("\nPlease Type only '1' or '2'")


def high_follower_count(follower_count_1, follower_count_2):
    count = 0
    if follower_count_1 > follower_count_2:
        count = 1
    else:
        count = 2
    return count
        

print(dataset.game_text.center(50))
print()

correct_count = 0
is_correct = True
high_count = 0

ques_1 = random.choice(dataset.data)
position_1 = dataset.data.index(ques_1)
dataset.data.pop(position_1)

while is_correct:

    ques_2 = random.choice(dataset.data)
    position_2 = dataset.data.index(ques_2)
    dataset.data.pop(position_2)

    print(f"\nCompare 1: {ques_1['name']}, {ques_1['description']}, from {ques_1['country']}")
    print(f'{dataset.vs_text}\n')
    print(f"Compare 2: {ques_2['name']}, {ques_2['description']}, from {ques_2['country']}")

    print(ques_1['follower_count'], ques_2['follower_count'])

    user_input = user_response()
    high_count = high_follower_count(ques_1['follower_count'], ques_2['follower_count'])

    if high_count == user_input:
        correct_count += 1
        os.system('cls')
        print(dataset.game_text)
        print(f"\nYou are right!! Your final Score is {correct_count}")
        ques_1 = ques_2
    else:
        os.system('cls')
        print(dataset.game_text)
        print(f"\nYou are wrong... Your final Score is {correct_count}")
        is_correct = False

print('\nThank You!')

