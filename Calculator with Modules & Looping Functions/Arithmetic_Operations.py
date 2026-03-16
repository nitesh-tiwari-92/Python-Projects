

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
        # with open('Error_Logger.log', 'r') as fr: 
        #     data = fr.read()

        # with open(r'C:\Users\Nitesh_Tiwari\Downloads\Error_Log.txt', 'w') as fw:
        #     fw.write(data)

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


# def mul_add(statement):

#     # user_num = input(statement).split(' ')
#     # if len(user_num) <= 1:

#     #     try:
#     #         if user_num[0].isnumeric():
#     #             user_num[0] = int(user_num[0])
#     #         else:
#     #             user_num[0] = float(user_num[0])

#     #         if user_num[0] >= 10:
#     #             user_ch = continuation("Do you want the numbers to be separated individually and after perform the addition? (Y/N): ")

#     #             if user_ch == 'Y':
#     #                 user_num = list(str(user_num[0]))
#     #                 user_num = [int(num) for num in user_num]

#     #                 result = 0
#     #                 for i in user_num:
#     #                     result += i
#     #             # print(f"The Addition of the Individual Digits of the Number is: {result}\n")

#     #             else:
#     #                 return mul_add(statement)

#     #         else:
#     #             return mul_add(statement)
#     #         # else:
                
#     #     except Exception:
#     #         print("Please Enter a Valid Numeric Number.\n")
#     #         return mul_add(statement)

#     # else:
#     #     print("Please Enter Only One Number for this Operation.\n")
#     #     return mul_add(statement)

#     while True:

#         user_num = input(statement).split(' ')

#         try:
#             num = int(user_num[0])

#         except ValueError:
#             print("Please Enter a Valid Integer Number.\n")
#             continue

#         if num < 10:
#             print("Number must be 10 or greater.\n")
#             continue

#         user_ch = continuation("Do you want the digits to be separated and added? (Y/N): ")

#         if user_ch == 'Y':

#             digits = [int(d) for d in str(num)]
#             result = sum(digits)

#             print(f"The Addition of the Individual Digits is: {result}\n")
#             return result

#         else:
#             print("Operation cancelled.\n")
#             return None

#         if len(user_num) > 1:
#             print("Please Enter Only One Number for this Operation.\n")
#             continue



# def factorial():
#     fact_1 = 1
#     fact_2 = 1
#     for i in range(1, num_1 + 1):
#         fact_1 *= i
#     for j in range(1, num_2 + 1):
#         fact_2 *= j
#     print(f"Factorial of {num_1} is:", fact_1)
#     print(f"Factorial of {num_2} is:", fact_2)
#     return print("\nThe Factorial of the Two Numbers is:", fact_1, "and", fact_2,"\n")