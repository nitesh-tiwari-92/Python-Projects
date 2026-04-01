

from User_Input import single_input, double_input, continuation # Calling function to get the Input from User via user_input() function from User_Input.py file
import logging



def add():

    num_1, num_2 = double_input() # Getting the two numbers from user via double_input() function from User_Input.py file
    
    print(f"{num_1} + {num_2} =", num_1 + num_2)
    return print("\nThe Addition of the Two Numbers is:", num_1 + num_2,"\n")


def mul():
    
    num_1, num_2 = double_input()
    
    print(f"{num_1} * {num_2} =", num_1 * num_2)
    return print("\nThe Multiplication of the Two Numbers is:", num_1 * num_2,"\n")


def exp():
    
    num_1, num_2 = double_input()
    
    print(f"{num_1} ** {num_2} =", num_1 ** num_2)
    return print("\nThe Exponentiation of the Two Numbers is:", num_1 ** num_2,"\n")


def sub():

    num_1, num_2 = double_input()

    if num_1 >= num_2:

        print(num_1, '-', num_2, "=", num_1 - num_2)
        return print(f"\nThe Subtraction of the Two Numbers is:", num_1 - num_2, "\n")

    else:
        print('''\nThe first number is smaller than the second number.
        \nSwitching the order of the numbers to perform subtraction...\n''')
        print(f"{num_2} - {num_1} =", num_2 - num_1,'\n')


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


def mul_add(*num):

    user_nums = mul_input(*num)
    sum = 0
    
    for n in user_nums:
        sum += n
    
    return print(f'\nThe addition of provided all numbers is {sum}\n')


def mul_mul(*num):

    user_nums = mul_input(*num)
    mul = 1
    
    for n in user_nums:
        mul *= n
    
    return print(f'\nThe multiplication of provided all numbers is {mul}\n')
