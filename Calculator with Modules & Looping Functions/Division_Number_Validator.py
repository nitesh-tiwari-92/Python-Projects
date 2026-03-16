

import logging
from User_Input import double_input # Calling function to get the Input from User via user_input() function from User_Input.py file


def div():

    num_1, num_2 = double_input()

    try:
        print(f"{num_1} / {num_2} =", num_1 / num_2)
        return print("\nThe Division of the Two Numbers is:", num_1 / num_2,'\n')

    except ZeroDivisionError:
        print("The second provided number must be greater than Zero (0).\n")

        logging.error("Attempted to divide by zero.", exc_info=True)

    except Exception as e:
        print(f"\nSomething went wrong. Please try again. Error: {e}\n")
        logging.error("An error occured while Division", exc_info=True)


def mod():

    num_1, num_2 = double_input()

    try:
        print(f"{num_1} % {num_2} =", num_1 % num_2)
        return print("\nThe Modulus of the Two Numbers is:", num_1 % num_2,"\n")
    
    except ZeroDivisionError:
        print("The second provided number must be greater than Zero (0).\n")
        logging.error("Attempted to modulus by zero.", exc_info=True)

    except Exception as e:
        print(f"\nSomething went wrong. Please try again. Error: {e}\n")
        logging.error("An error occured while Modulus", exc_info=True)


def floor_div():

    num_1, num_2 = double_input()

    try:
        print(f"{num_1} // {num_2} =", num_1 // num_2)
        return print("\nThe Floor Division of the Two Numbers is:", num_1 // num_2,"\n")
    
    except ZeroDivisionError:
        print("The second provided number must be greater than Zero (0).\n")
        logging.error("Attempted to floor divide by zero.", exc_info=True)

    except Exception as e:
        print(f"\nSomething went wrong. Please try again. Error: {e}\n")
        logging.error("An error occured while Floor Division", exc_info=True)
