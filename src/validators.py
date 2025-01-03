from constants import NAME_REGEX, GRADES, SUBJECTS
from user_input_functions import get_user_selection
import re
from datetime import datetime


# ==========================
# Validator Functions
# ==========================

def validate_names(prompt):
    while True:
        names = input(prompt).title()
        cleaned_names = ' '.join(names.strip().split())
        if re.match(NAME_REGEX, cleaned_names, re.UNICODE):
            return cleaned_names
        else:
            print("Invalid input. Please enter valid names consisting of letters or hyphen only.")


def get_valid_names():
    first_and_last_names = validate_names("Enter student's full name: ")
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


def validate_student_subject():
    
    subject_keys = list(SUBJECTS.keys())

    print("Please select the subject to add the grade for")

    index = 1
    for key in subject_keys:
        print(f"{index}. {SUBJECTS[key]}")
        index += 1
    user_selection = get_user_selection(1, 17)
    student_subject = subject_keys[user_selection - 1]
    return student_subject

def validate_student_grade():

    while True:
        try:
            user_input_grade = input("Enter students grade (U - 9): ")
            if user_input_grade in GRADES:
                return user_input_grade
            else:
                continue
        except ValueError:
            print(f"{user_input_grade} is not a valid grade")
