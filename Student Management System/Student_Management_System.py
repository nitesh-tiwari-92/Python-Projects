

students_data = {
    1234: [{'Name':['Nitesh', 'Tiwari']}, 'CSE', [{'Maths': 88}, {'Science': 54}, {'English': 33}, {'Computer': 55}, {'Physics': 67}]],
    1235: [{'Name':['Aarav', 'Sharma']}, 'ECE', [{'Maths': 92}, {'Science': 78}, {'English': 85}, {'Computer': 80}, {'Physics': 89}]],
    1236: [{'Name':['Ishani', 'Verma']}, 'ME', [{'Maths': 74}, {'Science': 65}, {'English': 90}, {'Computer': 60}, {'Physics': 72}]],
    1237: [{'Name':['Vihaan', 'Gupta']}, 'CSE', [{'Maths': 85}, {'Science': 88}, {'English': 72}, {'Computer': 95}, {'Physics': 84}]],
    1238: [{'Name':['Ananya', 'Singh']}, 'IT', [{'Maths': 68}, {'Science': 70}, {'English': 95}, {'Computer': 88}, {'Physics': 65}]],
    1239: [{'Name':['Arjun', 'Mehta']}, 'CE', [{'Maths': 55}, {'Science': 60}, {'English': 58}, {'Computer': 50}, {'Physics': 62}]],
    1240: [{'Name':['Sanya', 'Malhotra']}, 'ECE', [{'Maths': 91}, {'Science': 82}, {'English': 89}, {'Computer': 77}, {'Physics': 85}]],
    1241: [{'Name':['Rohan', 'Joshi']}, 'CSE', [{'Maths': 45}, {'Science': 52}, {'English': 60}, {'Computer': 70}, {'Physics': 48}]],
    1242: [{'Name':['Kavya', 'Iyer']}, 'EE', [{'Maths': 88}, {'Science': 94}, {'English': 82}, {'Computer': 85}, {'Physics': 90}]],
    1243: [{'Name':['Aditya', 'Rao']}, 'ME', [{'Maths': 72}, {'Science': 70}, {'English': 65}, {'Computer': 68}, {'Physics': 75}]],
    1244: [{'Name':['Meera', 'Nair']}, 'IT', [{'Maths': 79}, {'Science': 85}, {'English': 92}, {'Computer': 94}, {'Physics': 81}]],
    1245: [{'Name':['Dev', 'Patel']}, 'CE', [{'Maths': 63}, {'Science': 58}, {'English': 55}, {'Computer': 60}, {'Physics': 59}]],
    1246: [{'Name':['Tara', 'Khanna']}, 'CSE', [{'Maths': 95}, {'Science': 91}, {'English': 88}, {'Computer': 98}, {'Physics': 93}]],
    1247: [{'Name':['Kabir', 'Bansal']}, 'ECE', [{'Maths': 82}, {'Science': 76}, {'English': 70}, {'Computer': 72}, {'Physics': 80}]],
    1248: [{'Name':['Zoya', 'Khan']}, 'EE', [{'Maths': 77}, {'Science': 80}, {'English': 85}, {'Computer': 82}, {'Physics': 79}]],
    1249: [{'Name':['Aryan', 'Chopra']}, 'ME', [{'Maths': 60}, {'Science': 64}, {'English': 68}, {'Computer': 55}, {'Physics': 61}]],
    1250: [{'Name':['Kiara', 'Advani']}, 'IT', [{'Maths': 84}, {'Science': 78}, {'English': 90}, {'Computer': 86}, {'Physics': 82}]],
    1251: [{'Name':['Siddharth', 'Malhotra']}, 'CSE', [{'Maths': 89}, {'Science': 85}, {'English': 80}, {'Computer': 92}, {'Physics': 88}]],
    1252: [{'Name':['Riya', 'Sen']}, 'ECE', [{'Maths': 67}, {'Science': 72}, {'English': 75}, {'Computer': 70}, {'Physics': 68}]],
    1253: [{'Name':['Varun', 'Dhawan']}, 'ME', [{'Maths': 58}, {'Science': 62}, {'English': 60}, {'Computer': 65}, {'Physics': 55}]],
    1254: [{'Name':['Sara', 'Ali']}, 'CE', [{'Maths': 75}, {'Science': 80}, {'English': 82}, {'Computer': 78}, {'Physics': 77}]],
    1255: [{'Name':['Kartik', 'Aryan']}, 'CSE', [{'Maths': 92}, {'Science': 88}, {'English': 85}, {'Computer': 95}, {'Physics': 90}]],
    1256: [{'Name':['Janhvi', 'Kapoor']}, 'IT', [{'Maths': 81}, {'Science': 84}, {'English': 88}, {'Computer': 82}, {'Physics': 85}]],
    1257: [{'Name':['Ishan', 'Khattar']}, 'EE', [{'Maths': 70}, {'Science': 68}, {'English': 72}, {'Computer': 75}, {'Physics': 71}]],
    1258: [{'Name':['Ananya', 'Pandey']}, 'ECE', [{'Maths': 65}, {'Science': 60}, {'English': 78}, {'Computer': 70}, {'Physics': 62}]],
    1259: [{'Name':['Ranbir', 'Kapoor']}, 'ME', [{'Maths': 88}, {'Science': 92}, {'English': 85}, {'Computer': 80}, {'Physics': 94}]],
    1260: [{'Name':['Alia', 'Bhatt']}, 'CSE', [{'Maths': 94}, {'Science': 95}, {'English': 98}, {'Computer': 99}, {'Physics': 92}]],
    1261: [{'Name':['Vicky', 'Kaushal']}, 'CE', [{'Maths': 72}, {'Science': 74}, {'English': 70}, {'Computer': 68}, {'Physics': 75}]],
    1262: [{'Name':['Katrina', 'Kaif']}, 'IT', [{'Maths': 80}, {'Science': 78}, {'English': 85}, {'Computer': 88}, {'Physics': 82}]],
    1263: [{'Name':['Ranveer', 'Singh']}, 'ECE', [{'Maths': 85}, {'Science': 82}, {'English': 80}, {'Computer': 84}, {'Physics': 87}]]
}


def number_conversion(statement):
    
    try:
        number = input(statement)
        number = int(number)

    except:
        print('Invalid Input. Please try Again...')
        return number_conversion(statement)

    return number


def task_confirmation(statement):

    confirm = input(statement).lower()
    return confirm

 
def task_operation():

    task_code = number_conversion('\nEnter your Operation Code: ')

    if task_code == 1: # Add

        while True:
            student_id = number_conversion('\nEnter Student Roll Number/ID: ')

            if student_id in students_data:
                print('\nStudent Roll Number/ID already available! Please Enter different ID: ')

            else:
                fname = input('\nEnter Student First Name: ')
                lname = input('Enter Student Last Name: ')
                department = input('\nEnter Student Departmnent Name: ')
                subject_list = []

                for sub in range(5):
                        subject = input('\nEnter Subject Name: ')
                        mark = number_conversion('Enter Marks: ')
                        subject_list.append({subject: mark})

                students_data[student_id] = [{'Name': [fname, lname]}, department, subject_list]

                print('\nStudent Record created Successfully.')
                print(students_data[student_id])

            confirmation = task_confirmation('\nDo you want to perform another Operation? [Y/N]: ')
            if confirmation in ['y', 'yes', 'ye']:
                task_operation()
            else:
                exit()

    elif task_code == 2: # Edit

        student_id = number_conversion('\nEnter Student Roll Number: ')
        student_detail = students_data.get(student_id, 'Not Found')

        if student_detail != 'Not Found':
            print('\nWhich Information you want to Edit?')

            for i, value in enumerate(['Name', 'Department', 'Subject', 'Marks'], 1):
                print(f'{i} - {value}')

            modification_detail = number_conversion('\nPlease provide the field (1 - 4) for modification: ')
            if modification_detail == 1:
                student_detail[0]['Name'][0] = input('\nPlease enter Student First Name: ').title()
                student_detail[0]['Name'][1] = input('Please enter Student Last Name: ').title()

            elif modification_detail == 2:
                student_detail[1] = input('\nPlease enter the Student New Department: ').upper()

            elif modification_detail == 3:
                subject = input('\nWhich Subject you want to replace with? ').title() 
                subject_found = False
                for subjects in student_detail[2]:

                    for sub, mark in subjects.items():
                        if subject == sub:
                            new_subject = input('\nEnter New Subject Name: ').title()
                            subjects[new_subject] = subjects.pop(sub)
                            subject_found = True
                            break

                    if subject_found == True:
                        break

                if subject_found == False:
                    print('\nSubject not available for the selected Student ID')
            else:
                subject = input('\nWhich Subject Marks you want to update? ').title() 
                subject_found = False
                for subjects in student_detail[2]:

                    for sub, mark in subjects.items():
                        if subject == sub:
                            new_marks = float(number_conversion('Enter updated Marks: '))
                            subjects[sub] = new_marks
                            subject_found = True
                            break

                    if subject_found == True:
                        break

                if subject_found == False:
                    print('\nSubject not available for the selected Student ID')
        else:
            print('\nStudent Record Not Found!')

        confirmation = task_confirmation('\nDo you want to perform another Operation? [Y/N]: ')
        if confirmation in ['y', 'yes', 'ye']:
            task_operation()
        else:
            exit()

    elif task_code == 3: # Delete

        student_id = number_conversion('\nEnter Student Roll Number: ')
        student_detail = students_data.get(student_id, 'Not Found')

        if student_detail != 'Not Found':

            for detail in range(len(student_detail)):

                if detail == 0:
                    name = student_detail[0]['Name'][0] + ' ' + student_detail[0]['Name'][1]
                    print(f'\nStudent Name: {name}')

                elif detail == 1:
                    print(f'\nDepartment: {student_detail[1]}')

                else:
                    print('\nScored Marks in each Subject: \n')
                    for subjects in student_detail[2]:

                        for subject, marks in subjects.items():
                            print(f'{subject}: {marks}')

            confirmation = task_confirmation('\nPlease confirm! Do you want to delete the student record?: ')

            if confirmation in ['y', 'yes', 'ye']:
                del students_data[student_id]
                print(f'\nStudent Record {student_id} deleted successfully.')
            else:
                print('\nInavalid Confirmation Input!')
                print('Exiting the Operation ..')

        else:
            print('Student Record Not Found!')

        confirmation = task_confirmation('\nDo you want to perform another Operation? [Y/N]: ')

        if confirmation in ['y', 'yes', 'ye']:
            task_operation()
        else:
            exit()

    elif task_code == 4: # View

        student_id = number_conversion('\nEnter Student Roll Number: ')
        student_detail = students_data.get(student_id, 'Not Found')

        if student_detail != 'Not Found':

            name = student_detail[0]['Name']
            print(f'\nStudent Name: {name[0]} {name[1]}')
            print(f'\nDepartment: {student_detail[1]}')
            print('\nScored Marks in each Subject: \n')

            for subjects in student_detail[2]:

                for subject, marks in subjects.items():
                    print(f'{subject}: {marks}')

        else:
            print('\nStudent Record Not Found!')

        confirmation = task_confirmation('\nDo you want to perform another Operation? [Y/N]: ')

        if confirmation in ['y', 'yes', 'ye']:
            task_operation()

        else:
            exit()

    elif task_code == 5: # Search

        student_id = number_conversion('\nEnter Student Roll Number: ')
        student_detail = students_data.get(student_id, 'Not Found')

        if student_detail != 'Not Found':
            print('Student details are available.')

        else:
            print('Student Record Not Found!')

        confirmation = task_confirmation('\nDo you want to perform another Operation? [Y/N]: ')

        if confirmation in ['y', 'yes', 'ye']:
            task_operation()

        else:
            exit()

    elif task_code == 6: # Exit
        print('Thank You !')
        exit()

    else:
        print('Invalid Operation Code provided. Try Again !')
        task_operation()

    return task_code


print(' Student Management System '.center(100, '-'))
print('')
print('Which operation you want to perform: ')

for i, operation in enumerate(['Add', 'Edit', 'Delete', 'View', 'Search', 'Exit'], 1):
    operation += ' Student'
    if i == 6:
        print(f'{i} - Exit')
    else:
        print(f'{i} - {operation.title()}')

task_operation()
