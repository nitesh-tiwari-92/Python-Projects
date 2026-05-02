
## Number Pyramid

print("Welcome to the Number Pyramid.")

cont = 'y'
while cont in ('y', 'yes'):

    row_num = input("\nEnter the number of rows for the pyramid (positive integer): ") 
    try:
        row_num = int(row_num)
        avg = row_num - 1    
        if row_num <= 20:
            print("\nHere is your number pyramid:\n")

            for i in range(1, row_num + 1):
                print(" " * row_num, end=' ')

                for j in range(1, i + 1):
                    print(j, end=' ')
                
                row_num -= 1
                print() # New line after each row - help

        else:
            print("\nThe maximum allowed levels is 20. Please enter the number less than 20.")
    
    except :
        print("\nInvalid Input. Please enter a positive integer value.")

    cont = input("\nWould you like to create another pyramid? (y/n): ").lower()

print("Exit")

