# ==========================
# Constants
# ==========================

# Subjects with readable mapping
SUBJECTS = {
    "maths": "Mathmatics",
    "english": "English",
    "biology": "Biology",
    "physics": "Physics",
    "chemistry": "Chemistry",
    "physical_education": "Physical Education",
    "history": "History",
    "religous_education": "Religious Education",
    "geography": "Geography",
    "food_tech": "Food Technology",
    "textiles": "Textiles",
    "design_technology": "Design Technology",
    "foreign_languages": "Foreign Languages",
    "art_and_design": "Art and Design",
    "music": "Music",
    "citizenship": "Citizenship",
    "information_technology": "Information Technology"
}

GRADES = ("9", "8", "7", "6", "5", "4", "3", "2", "1", "U")

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
INTERNAL_HEADERS = {v: k for k, v in READABLE_HEADERS.items()}
