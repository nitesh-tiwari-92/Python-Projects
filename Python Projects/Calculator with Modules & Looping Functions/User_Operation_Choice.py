

import logging
import User_Input


def choice(statement):
    
    user_choice = User_Input.single_input(statement) # Getting the choice of the user for single input operation
    
    if user_choice in [1, 2, 3]:
        return user_choice

    else:
        logging.error(f"Invalid choice entered: {user_choice}")
        return None
        


def operation(statement, choice_type):
    
    if choice_type == 1:

            print('''\nYou have selected Operation with Single Input.\n
The available operations for Single Input are:\n
1. Square Root
2. Cube\n''')

            user_choice = User_Input.single_input(statement)
            
    elif choice_type == 2:

            print('''\nYou have selected Operation with Double Input.\n
The available operations for Double Input are:\n
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Modulus
7. Floor Division\n''')
            user_choice = User_Input.single_input(statement)

    elif choice_type == 3:

            print('''\nYou have selected Operation with Multiple Input.\n
The available operations for Multiple Input are:\n
1. Addition
2. Multiplication\n''')
            user_choice = User_Input.single_input(statement)

    else:
            logging.error(f"Invalid choice entered: {choice_type}")
            return None

    return user_choice
