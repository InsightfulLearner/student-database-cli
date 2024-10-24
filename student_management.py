from validators import get_valid_names, get_valid_date_of_birth
from user_input_functions import get_user_selection, handle_user_selection, exit_program
from data_management import save_to_csv
from student_data import student_data
import random


# ==========================
# Unique ID Generation
# ==========================

# Create unique ID for each student
def create_unique_id(full_name):
    existing_uids = {student['unique_id'] for student in student_data.values()}
    initials = ''.join(part[0] for part in full_name.split())  # Extract initials from the full name

    while True:
        random_numbers = ''.join(random.choices('0123456789', k=6))
        unique_id = f"{initials.upper()}{random_numbers}"  # Ensure uppercase initials

        if unique_id not in existing_uids:
            return unique_id  # Return as soon as we find a unique ID


# ==========================
# Student Management Functions
# ==========================


def student_management():

    from display_functions import show_menu
    from display_functions import show_list_of_students
    from search_functions import search_for_student

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
    print("Current student data:", student_data)  # Debugging statement
    save_to_csv()


def print_student_data(student):

    print(
        f"Unique ID: {student['unique_id']}, "
        f"Student's Name: {student['student_names']}, "
        f"Date of Birth: {student['student_dob']}"
        )


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

# Remove student from database (add confirmation