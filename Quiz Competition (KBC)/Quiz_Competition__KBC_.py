


import Questions
import random
import os



def user_input_check(statement):

    try:
        ans_check = input(statement)
        ans_check = int(ans_check)

        if ans_check in range(1,5):
            return ans_check 
        
        else:
            print('Oops! That’s not a valid option. Please enter a number between 1 and 4.')
            return user_input_check(statement)

    except ValueError:

        print('Oops! That’s not a valid option. Please enter a number between 1 and 4.')
        return user_input_check(statement)

    except Exception:

        print('Invalid input detected. Kindly select an option between 1 and 4.')
        return user_input_check(statement)


print(('*'*35).center(100))
print('Welcome to Quiz (KBC) Game'.center(100))
print(('*'*35).center(100))
print("\n" + "QUIZ RULES".center(100, "-"))
print("\n" + "You will get 5 attempts to prove your skills!".center(100))
print("Each attempt = 20 unique questions.".center(100))
print("Use them wisely — once all attempts are exhausted, the quiz will end.".center(100))
print("Don't worry, everything resets for a fresh start next time!".center(100))
print('\n' + 'Enter your choice between 1 - 4'.center(100))
print("-"*100)


attempt = 1
questions_correct = 0
questions_list = []

while attempt <= 5:

    print('\n' + f'Attempt No.: {attempt}'.center(100))
    
    for questions in range(1, 21):

        question = random.choice(Questions.quiz_questions)

        question_index = Questions.quiz_questions.index(question)
        Questions.quiz_questions.pop(question_index)

        print(f'\nQuestion {questions}: {question[0]}')

        for i, options in enumerate(question[1], 1):
            print(f'{i}. {options}')

        user_ans = user_input_check('\nEnter your Choice (1 - 4): ')

        if user_ans == (question[2] + 1):
            print('Correct Answer! 😊')
            questions_correct += 1
            question.append('Correct')
            

        else:
            print('Wrong Answer 😔')
            print(f'Correct Answer: {question[2] + 1}')
            question.append('Incorrect')
            
        questions_list.append(list(question))
    
    print('\n' + ' Result '.center(100, '-'))
    print(f'Attempt No.: {attempt}')
    print('Total Questions: 20')
    print(f'Total Correct Questions: {questions_correct}')
    print(f'Total Incorrect Questions: {20 - questions_correct}')
    
    user_cont = input('\nDo you want to play again (Y/N): ').lower()

    if user_cont in ['y', 'yes', 'ye']:

        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        break

    attempt += 1
