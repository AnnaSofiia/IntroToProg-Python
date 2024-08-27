# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Anna-Sofiia Mykhalevych, 26.08.2024, Modified to add error handling
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments05.csv"

# Data Variables and constants
# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list = []  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# Initial file read
try:
    with open(FILE_NAME, "r") as file:
        for row in file:
            student_data = row.strip().split(',')
            students.append(student_data)
except FileNotFoundError:
    print("Text file must exist before running this script")
    print("-- Technical Error Message -- ")
    print("Please make sure the file 'Enrollments05.csv' is in the current directory.")
except Exception as e:
    print("There was a non-specific error!")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')

# Menu presentation and processing data
while True:
    print(MENU)
    menu_choice = input("What would you like to do: ").strip()

    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers or special characters.")
            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers or special characters.")
            course_name = input("Please enter the name of the course: ").strip()
            students.append([student_first_name, student_last_name, course_name])
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print("An unexpected error occurred:", e)

    elif menu_choice == "2":
        print("-" * 50)
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        print("-" * 50)

    elif menu_choice == "3":
        try: 
            with open(FILE_NAME, "w") as file:
                for student in students:
                    csv_data = f"{student[0]},{student[1]},{student[2]}\n"
                    file.write(csv_data)
            print("Data has been saved to the file.")
        except Exception as e:
            print("Failed to save data to file:")
            print(e, e.__doc__, type(e), sep='\n')

    elif menu_choice == "4":
        print("Program Ended")
        break

    else:
        print("Please only choose option 1, 2, or 3")