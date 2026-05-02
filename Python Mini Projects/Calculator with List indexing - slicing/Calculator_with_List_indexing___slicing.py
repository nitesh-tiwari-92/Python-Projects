

username = input("Your Full Name: ")
print(f"\nWelcome '{username}' to the Calculator!")

def user_value(prompt):

    while True:

        value = input(prompt)
        try:
            value = eval(value)
            return value

        except: 
            print("\nInvalid input. Please enter a numeric value.")
            

def calculation(number_1, number_2, symbol_name):

    if symbol_name == '+' or symbol_name == 'addition':
        result = number_1 + number_2

    elif symbol_name == '-' or symbol_name == 'subtraction':
        result = number_1 - number_2

    elif symbol_name == '*' or symbol_name == 'multiplication':
        result = number_1 * number_2

    elif symbol_name == '//' or symbol_name == 'floor division':
        result = number_1 // number_2
        
    elif symbol_name == '%' or symbol_name == 'modulus':
        result = number_1 % number_2
        
    elif symbol_name == '/' or symbol_name == 'division':
        result = number_1 / number_2

    else:
        result = number_1 ** number_2
    
    print("\nCalculating...")
    return print(f"\nThe {symbol_name.capitalize()} of your 2 numbers, {number_1} & {number_2} is: {result}")


def operation():
    
    user_input = input("\nPlease enter the Operation/Calculation you want to make: ").lower()

    try:
        user_input = int(user_input)
        if user_input in [1, 2, 3, 4, 5, 6, 7]:
            return calculation(number_1 = num_1, number_2 = num_2, symbol_name = operation_name[user_input - 1])

        else:
            print('Invalid operation selection')
            operation()

    except :

        if user_input in operation_name:
            return calculation(num_1, num_2, user_input)

        elif user_input in operation_symbol:
            op_sym = operation_symbol.index(user_input)
            op_name = operation_name[op_sym]
            return calculation(num_1, num_2, op_name)

        else:
            print('Invalid operation selection')
            return operation()


operation_symbol = ['+','-','*','/','//','%','**']

operation_name = ["addition", "subtraction", "multiplication", "division", "floor division", "modulus", "exponent"]

continuation = 'y'

while continuation in ['y', 'yes', 'ye']:
   
    num_1 = user_value("\nEnter the first number of your choice: ")
    num_2 = user_value("Enter the second number of your choice: ")

    print("\nChoose an operation from below list:")

    for i, on in enumerate(operation_name, 0):    
        print(f"{i + 1} - {operation_name[i].capitalize()} ({operation_symbol[i]})")
 
    operation()

    continuation = input('\nDo you want to continue [Y/N]: ')
