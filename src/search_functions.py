from student_data import student_data
from student_management import get_user_selection, handle_user_selection, print_student_data

# ==========================
# Search Functions
# ==========================

def search_for_student():
    from main import student_management
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