import sys
import csv
import random
import re
from datetime import datetime

student_data = [] # Create an initial variable to store/handle data input

# ==========================
# Constants
# ==========================


# Readable header mapping
READABLE_HEADERS = {
    "student_names": "Student Name",
    "unique_id": "Student ID",
    "student_dob": "Date of Birth",
    "student_address": "Address",
    "student_grades": "Grades",
    "student_absences": "Absences",
    "medical_appointments": "Medical Appointments",
    "medical_notes": "Medical Notes",
    "student_detentions": "Detentions",
    "emergency_contact": "Emergency Contact",
    "parents_names": "Parent Name",
}


NAME_REGEX = r'^[a-zA-Z- ]+$'

# Inverse mapping for loading data
internal_headers = {v: k for k, v in READABLE_HEADERS.items()}

# ==========================
# Data Loading
# ==========================

# Open file/load data from file or create relevant variable to store details to save to the file
def load_from_csv():
    global student_data
    try:
        with open("student_database.csv", "r") as file:
            reader = csv.DictReader(file)
            student_data = []
            for row in reader:
                student_data.append({internal_headers[key]: value for key, value in row.items()})
    except FileNotFoundError:
        print("File not found")
    except:
        print("Investigate error type - please report this")


# ==========================
# File Operations
# ==========================

def save_to_csv():
    with open("student_database.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldsnames=READABLE_HEADERS.values())
        writer.writeheader()

        for student in student_data:
            writer.writerow(student)


# ==========================
# Unique ID Generation
# ==========================

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


# ==========================
# Validator Functions
# ==========================

def validate_names(prompt):
    while True:
        names = input(prompt).title()
        cleaned_names = ' '.join(names.strip().split())
        if re.match(NAME_REGEX, cleaned_names, re.UNICODE):
            return cleaned_names.split()
        else:
            print("Invalid input. Please enter valid names consisting of letters or hyphen only.")


def get_valid_names():
    first_and_last_names = validate_names("Enter student's full name: ")
    uid = create_unique_id(first_and_last_names)
    return first_and_last_names


def validate_real_date(day, month, year):
    todays_date = datetime.now()
    current_year = todays_date.year
    try:
        student_dob = datetime(year, month, day)
    except:
        ValueError
        return False
    if (current_year - student_dob.year) < 22:
        return student_dob
    else:
        return False


def get_valid_date_of_birth():
    while True:
        dob_input = input("Enter student's date of birth (DD-MM-YYYY): ")
        if re.match(r'^\d{2}-\d{2}-\d{4}$', dob_input): # Check for correct format
            day, month, year = map(int, dob_input.split('-'))
            if validate_real_date(day, month, year):
                return dob_input 
        print("Invalid date format or date is not valid. Please use DD-MM-YYYY")


# ==========================
# Student Management Functions
# ==========================

# Add student to database 
# Unique ID, Name, DOB, Address, Grades by subject, abscences, medical notes, detentions
# Parent/Guardian and their contact details
def add_student():
    get_student_names = get_valid_names() # Gets the user to input the students name (has validation checks)
    uid = create_unique_id(get_student_names)
    get_date_of_birth = get_valid_date_of_birth()

    student = {
        "student_names": get_student_names,
        "unique_id": uid,
        "student_dob": get_date_of_birth
    }
    student_data.append(student)
    for student in student_data:
        print(student)


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


# ==========================
# Display Functions
# ==========================

# View all students in database (show all students and info)
def show_list_of_students():

    if not student_data: # Check if the list is empty
        print("No students found")
        return
    
    try:
        for student in student_data:
            print(
            f"Unique ID: {student['unique_id']} "
            f"Student's Name: {' '.join(student['student_names'])} "
            f"Date of Birth: {student['student_dob']}"
            )
    except KeyError as e:
        print(f"Missing key: {e}")
    except Exception as e:
        print(f"An error occurred {e}")


# ==========================
# Search Functions
# ==========================

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
        "5. Go back to Menu"
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

# ==========================
# Main Menu Functions
# ==========================

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
    show_menu()
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


# ==========================
# User Input Functions
# ==========================

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


# ==========================
# Main Function
# ==========================
def main():
    load_from_csv()
    while True:
        student_management() # Initial menu and user input handling


if __name__ == "__main__":
    main()