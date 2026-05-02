

from User_Input import double_input # Calling function to get the Input from User via user_input() function from User_Input.py file



def sub():

    num_1, num_2 = double_input()

    if num_1 > num_2:

        print(num_1, '-', num_2, "=", num_1 - num_2)
        return print(f"\nThe Subtraction of the Two Numbers is:", num_1 - num_2, "\n")

    else:
        print("\nThe first number is smaller than the second number. Please provide a larger first number to perform subtraction.\n")