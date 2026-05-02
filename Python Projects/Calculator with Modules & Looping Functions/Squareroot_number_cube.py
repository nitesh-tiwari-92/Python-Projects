

from User_Input import single_input # Calling function to get the Input from User via user_input() function from User_Input.py file


def sqrt():

    num_1 = single_input("Enter your Number to find its Square Root: ")
    print(f"\nSquare Root of {num_1} is:", num_1 ** 0.5,'\n')


def cube():

    num_1 = single_input("Enter your Number to find its Cube: ")
    print(f"\nCube of {num_1} is:", num_1 ** 3,'\n')