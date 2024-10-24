from student_data import student_data
from student_management import print_student_data

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
