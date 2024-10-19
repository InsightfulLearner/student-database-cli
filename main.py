import sys
import csv
import random
import re

student_data = []

FIELDSNAMES = ["unique_id", "student_names", 
               "student_dob", "student_address", "student_grades", 
               "student_absences", "medical_appointments", "medical_notes", 
               "student_detenions", "emergency_contact", "parents_name"]

NAME_REGEX = r'^[a-zA-Z- ]+$'


# Open file/load data from file or create relevant variable to store details to save to the file
try:
    with open("student_database.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_data.append(row)
except FileNotFoundError:
    print("File not found")
except:
    print("Investigate error type - please report this")

# Save data to file
def save_to_file():
    with open("student_database.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldsnames=FIELDSNAMES)
        writer.writeheader()
        for student in student_data:
            writer.writerow(student)


# Validator functions


def validate_names(prompt):
    while True:
        names = input(prompt).strip().title()
        if re.match(NAME_REGEX, names, re.UNICODE):
            return names.split()
        else:
            print("Invalid input. Please enter valid names consisting of letters or hyphen only.")


def get_valid_names():
    first_and_last_names = validate_names("Enter student's full name: ")
    print(first_and_last_names)
    uid = create_unique_id(first_and_last_names)
    print(uid)
    return first_and_last_names


# Create unique ID for each student
def create_unique_id(first_and_last_names):
    exisiting_uids = {student['unique_id'] for student in student_data}
    initials = ""

    for name in first_and_last_names:
        initial = name[0]
        initials += initial

    while True:
        random_numbers = ''.join(random.choices('0123456789', k=6))
        unique_id = f"{initials}{random_numbers}"

        if unique_id in exisiting_uids:
            continue 
        else:
            break

    return unique_id

# Add student to database 
# Unique ID, Name, DOB, Address, Grades by subject, abscences, medical notes, detentions
# Parent/Guardian and their contact details
def add_student():
    get_valid_names() # Gets the user to input the students name (has validation checks)

def change_student_details():
    print("Work in progress")

def remove_student():
    print("Work in progress")

# Handle address input (potentially add a postcode look-up tool with manual entry)

# Add grade for subject (ask for the subject and grade + date achieved)

# Change grade for subject 

# Remove grade for subject (add confirmation)

# Store historical grades to see trends over time

# Add abscence including dates and reason

# Add medical appointments and notes

# Change medical appointments and notes

# Remove medical note (add confirmation)

# Add detention (date, duration, reason)

# Change detention (date, duration, reason)

# Remove detention (add confirmation)

# Add emergency contact (name, phone number, email address - optional)

# Change emergency contact

# Remove emergency contact (add confirmation)

# Remove student from database (add confirmation)

# View all students in database (show all students and info)
def show_list_of_students():

    if not student_data: # Check if the list is empty
        print("No students found")
        return
    
    try:
        for student in student_data:
            print(f"Unique ID: {student['unique_id']} "
                f"Student's Name: {student['student_names']} "
                f"Date of Birth: {student['student_dob']}"
                )
    except KeyError as e:
        print(f"Missing key: {e}")
    except Exception as e:
        print(f"An error occurred {e}")



def search_for_student():

    action_map = {
        1: search_by_name,
        2: search_by_unique_id,
        3: search_by_parents_name,
        4: search_by_dob,
        5: student_management
    }
    print("How would you like to search for the student?\n"
        "1. By Name (first, middle or last names)\n"
        "2. By Unique ID\n"
        "3. By Parent's Name\n"
        "4. By Date of Birth\n"
        "5. Go back to Menu\n"
    )
    user_selection = get_user_selection(1, 5)
    handle_user_selection(user_selection, action_map)

# Handles the logic to search for student's by any of their names
def search_by_name():
    print("Work in progress")

# Handles the logic to search for student's by their unique ID
def search_by_unique_id():
    print("Work in progress")

# Handles the logic to search for student's by their parents name
def search_by_parents_name():
    print("Work in progress")

# Handles the logic to search for student's by their date of birth
def search_by_dob():
    print("Work in progress")

# Shows the initial menu to the user for interaction
def show_menu() -> None:
    """
    Shows the user the menu and calls the user_selection function to get their input

    Returns:
        None
    """
    print("Student Database - Main Menu\n"
          "1. View list of students\n"
          "2. Search for a student\n"
          "3. Add a student to the database\n"
          "4. Add/Change a student's details in the database e.g. add a detention\n"
          "5. Remove a student from the database\n"
          "6. Exit"
          )


def student_management():
    action_map = {
        1: show_list_of_students,
        2: search_for_student,
        3: add_student,
        4: change_student_details,
        5: remove_student,
        6: exit_program,
    }
    user_selection = get_user_selection(1, 6)
    handle_user_selection(user_selection, action_map)


def get_user_selection(min_value: int = 1, max_value: int = 6) -> int:
    """
    Prompts the user for their input and returns their input.

    Returns:
        int: Returns the user's input as an int.
    """
    while True:
        try:
            user_selection = int(input("Please enter selection: "))
            if user_selection < min_value or user_selection > max_value:
                print(f"Please enter a valid selection between {min_value} and {max_value}")
            else:
                break
        except ValueError:
            print("You did not enter an integer")
    return user_selection


def handle_user_selection(user_selection, action_map):
    """
    Handles user selection based on the provided action map.

    Args:
        user_selection (int): The user's selection.
        action_map (dict): A mapping of user selection to functions.
    """
    action = action_map.get(user_selection)

    if action:
        action()  # Call the function associated with the selection
    else:
        print("Invalid selection.")


def exit_program() -> None:
    """
    This function when called will print 'exiting program' and exit the program.
    """
    print("Exiting program")
    sys.exit()


def main():
    while True:
        show_menu() # Show the user a list of options
        student_management() # Handle the users selection and call the relevant function


if __name__ == "__main__":
    main()