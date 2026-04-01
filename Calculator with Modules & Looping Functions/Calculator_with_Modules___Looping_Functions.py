

from Arithmetic_Operations import *
from Squareroot_number_cube import sqrt, cube
from User_Operation_Choice import choice, operation
from User_Input import continuation

# from Subtraction_Input_Validation import sub # not using this because it is already defined in Action.py and we are importing all the functions from Action.py using from Action import *
# from Division_Number_Validator import div, mod, floor_div # not using this because it is already defined in Action.py and we are importing all the functions from Action.py using from Action import *
 


print('''Please select the type of Input you want to proceed with:\n
1. Operation with Single Input
2. Operation with Double Input
3. Operation with Multiple Input\n''')

print('''Note:- Each opration has it's own set of operations, once you select your preferred choice, 
you need to select your desired operation from the list of operations you want to perform.\n''')

cont = 'Y' # Initializing the variable to control the while loop.'

while cont == 'Y':

    _choice_1 = choice("Enter your Choice: ") # Getting the choice of the user input type.
    _choice_2 = operation("Enter your Operation Code: ", _choice_1) # Getting the choice of the operation for the selected input choice.

    if _choice_1 == 1:

        if _choice_2 == 1:
            result = sqrt()
        
        elif _choice_2 == 2:
            result = cube()

    elif _choice_1 == 2:

        if _choice_2 == 1:
            result = add()
        
        elif _choice_2 == 2:
            result = sub()
        
        elif _choice_2 == 3:
            result = mul()
        
        elif _choice_2 == 4:
            result = div()
        
        elif _choice_2 == 5:
            result = exp()
        
        elif _choice_2 == 6:
            result = mod()
        
        elif _choice_2 == 7:
            result = floor_div()

    elif _choice_1 == 3:

        if _choice_2 == 1:
            result = mul_add()
        
        elif _choice_2 == 2:
            result = mul_mul()

    cont = continuation("Do you want to perform another operation? (Y/N): ")


print("Thank you for using the Calculator.")
