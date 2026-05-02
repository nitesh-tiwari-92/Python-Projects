

import os

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def operation():
    num1 = int(input('\nEnter your First Number: '))
    for op in oper_dict:
        print(op)

    cont = 'y'

    while cont:

        if cont == 'y':
            operator = input('\nPick an Operation: ')
            num2 = int(input('\nEnter your Second Number: '))
            _operation = oper_dict[operator]
            result = _operation(num1, num2)
            print(f'{num1} {operator} {num2} = {result}')
            num1 = result
            cont = input(f"\nenter 'y' to continue calculation with {result} or 'n' to start new calculation or 'x' to exit: ").lower()

        elif cont == 'n':
            os.system('cls')
            operation()
            cont = 'x'

        elif cont == 'x':
            print('\nThank You!')
            exit()

        else:
            exit()

oper_dict = {
    '+': add, 
    '-': subtract,
    '*': multiply,
    '/': divide
    }

operation()




# def operation(num1, operator, num2):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     else:
#         return num1 / num2

# def user_input(args):
#     num = int(input(args))
#     return num

# def operator(args):
#     opr = input(args)
#     if opr in ['+', '-', '*', '/']:
#         return opr
#     else:
#         print('Invalid selection of Operatios. Please select, +, -, *, /')
#         return operator(args)

# cont = 'y'
# num1 = user_input('Enter your First Number: ')
# while cont:
#     if cont == 'y':
#         _operator = operator('\n+ \n- \n* \n/ \n\nPick an Operation: ')
#         num2 = user_input('Enter your Second Number: ')
#         result = operation(num1, _operator, num2)
#         print(f'{num1} {_operator} {num2} = {result}')
#         print(f'enter \'y\' to continue calculation with {result} or "n" to start new calculation or "x" to exit: ')
#         num1 = int(result)
#         cont = input().lower()
#     elif cont == 'n':
#         num1 = user_input('Enter your First Number: ')
#         _operator = operator('\n+ \n- \n* \n/ \n\nPick an Operation: ')
#         num2 = user_input('Enter your Second Number: ')
#         result = operation(num1, _operator, num2)
#         print(f'{num1} {_operator} {num2} = {result}')
#         num1 = int(result)
#         print(f'enter \'y\' to continue calculation with {result} or "n" to start new calculation or "x" to exit: ')
#         cont = input().lower()
#     elif cont == 'x':
#         cont = 'x'
#         print('Thank You!')
#         exit()
#     else:
#         print('Exiting...')
#         exit()