


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

    user_ch = input(statement)
    if user_ch == 'Y' or user_ch == 'y':
        return user_ch.upper()
    else:
        exit
