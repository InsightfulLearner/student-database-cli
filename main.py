import sys
import csv
import random
from constants import SUBJECTS, GRADES, READABLE_HEADERS, INTERNAL_HEADERS
from validators import get_valid_names, get_valid_date_of_birth

student_data = {} # Create an initial variable to store/handle data input


# ==========================
# Data Loading
# ==========================

# Open file/load data from file or create relevant variable to store details to save to the file
def load_from_csv():
    global student_data
    try:
        with open("student_database.csv", "r") as file:
            reader = csv.DictReader(file)
            student_data = {}
            for row in reader:
                print(f"Row read: {row}")  # Debug: Show the raw row data
                uid = row["Student ID"].strip()  # Accessing the Student ID
                student_data[uid] = {
                    INTERNAL_HEADERS[header.strip()]: row[header].strip()  # Map each readable header to the internal key
                    for header in reader.fieldnames
                    if header.strip() in READABLE_HEADERS.values()  # Only include valid headers
                }
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Investigate error type - please report this: {e}")


# ==========================
# File Operations
# ==========================

def save_to_csv():
    with open("student_database.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=READABLE_HEADERS.values())
        writer.writeheader()

        for student in student_data.values():
            # Create a new dictionary that maps internal keys to readable keys
            row_to_write = {READABLE_HEADERS[key]: student[key] for key in student}
            writer.writerow(row_to_write)


# ==========================
# Unique ID Generation
# ==========================

# Create unique ID for each student
def create_unique_id(full_name):
    existing_uids = {student['unique_id'] for student in student_data}
    initials = ''.join(part[0] for part in full_name.split())  # Extract initials from the full name

    while True:
        random_numbers = ''.join(random.choices('0123456789', k=6))
        unique_id = f"{initials.upper()}{random_numbers}"  # Ensure uppercase initials

        if unique_id not in existing_uids:
            return unique_id  # Return as soon as we find a unique ID


# ==========================
# Student Management Functions
# ==========================

# Add student to database 
# Address, Grades by subject, abscences, medical notes, detentions
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
    student_data[uid] = student 
    save_to_csv()
    


def change_student_details():
    print("Work in progress")


def remove_student_by_unique_id():

    global student_data

    unique_id_input = input("Please enter the unique ID of the student to remove: ").upper()

    if unique_id_input in student_data:
        print("Student located: ", end="")
        print_student_data(student_data[unique_id_input])
        confirm_deletion = input("Would you like to remove this student? Y or N: ").upper().strip()
        if confirm_deletion == "Y":
            del student_data[unique_id_input]
            save_to_csv()
            print("Student removed from database")
        else:
            print("Student removal cancelled")
    else:
        print(f"Unable to locate student with unique ID: {unique_id_input}")


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
        for student in student_data.values():
            print_student_data(student)
    except KeyError as e:
        print(f"Missing key: {e}")
    except Exception as e:
        print(f"An error occurred {e}")


def print_student_data(student):

    print(
        f"Unique ID: {student['unique_id']}, "
        f"Student's Name: {student['student_names']}, "
        f"Date of Birth: {student['student_dob']}"
        )

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

    user_input = input("Please enter the student's name: ")

    found = False
    for student in student_data.values():
        if user_input.lower() in student ["student_names"].lower():
            print_student_data(student)
            found = True 
    if not found:
        print(f"No student found with the name {user_input}")


# Handles the logic to search for student's by their unique ID
def search_by_unique_id():
    user_input = input("Please enter the student's unique ID to search: ")

    if user_input in student_data.keys():
        print_student_data(student_data[user_input])
    else: 
        print(f"Unable to find student with unique ID: {user_input}")


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
        5: remove_student_by_unique_id,
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