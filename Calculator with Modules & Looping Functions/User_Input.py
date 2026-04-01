
def single_input(statement):

    try:     
        user_num = input(statement)
        if user_num.isnumeric():
            user_num = int(user_num)

        else:
            user_num = float(user_num)

        return user_num

    except ValueError:
        print("Please Enter a Valid Numeric Number.\n")
        return single_input(statement)

    except Exception as e:
        print(f"Error:", e, '\nPlease Try Again: \n')
        return single_input(statement)


def double_input():

    _num_1 = single_input("Enter your First Number: ")
    _num_2 = single_input("Enter your Second Number: ")

    return _num_1, _num_2


def continuation(statement):

    user_ch = input(statement).lower()
    if user_ch in ['y', 'ye', 'yes']:
        return user_ch
    else:
        exit


def separate():
    
    print('\nCalclulation with single number is not possible! Please provide atleast 2 number to perform the calculation.\n')
    ch = input("Do you want the numbers to be separated individually and after perform the addition? (Y/N): ").lower()

    if ch in ['y', 'yes', 'ye']:
        return ch

    else:
        print('Thank you for choosing the Nitesh\'s Calculator!!')
        print('Please comeback later.')
        exit
            

def mul_input(*numbers):
     
    try:
        user_input = (input('\nEnter your Numbers (separated by single (only one) blank space): ').strip()).lstrip()
        user_input = user_input.split(' ')

        for n in range(len(user_input)):

            if user_input[n] == '' or user_input[n].isspace():
                # user_input[n] = user_input[n].replace('', '0')
                # user_input[n] = int(user_input[n])
                print('\nPlease provide Numbers sepatated by only one/ single space (duplicate spaces in between are not allowed).\n')
                return mul_input(*numbers)

            elif user_input[n].isnumeric():
                user_input[n] = int(user_input[n])

            else:
                user_input[n] = float(user_input[n])

        if not len(user_input) >= 2:

            print('\nCalclulation with single number is not possible! Please provide atleast 2 number to perform the calculation.\n')
            ch = input("Do you want the numbers to be separated individually and after perform the calculation? (Y/N): ").lower()

            if ch in ['y', 'yes', 'ye']:
                lst = []
                user_input = str(user_input[0])
                # print(user_input, type(user_input), len(user_input))
                
                for n in range(len(user_input)):
                    lst.append(user_input[n])
                    lst[n] = int(lst[n])
                
                user_input = lst
                return user_input

            else:
                print('\nThank you for choosing the Nitesh\'s Calculator!!')
                print('Please comeback later.\n')
                exit()

        else:
            return user_input

    except ValueError:
        print("Please Enter a Valid Numeric Number.\n")
        return mul_input(*numbers)

    except Exception as e:
        print(f"Error:", e, '\nPlease Try Again: \n')
        return mul_input(*numbers)
