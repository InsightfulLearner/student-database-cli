import csv
import os
from constants import READABLE_HEADERS
from student_data import student_data


# ==========================
# File Operations
# ==========================

def save_to_csv():

    global student_data
    csv_file = "student_database.csv"

    try:
        with open(csv_file, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=READABLE_HEADERS.values())
            writer.writeheader()  # Write the header

            print("Student data (inside save_to_csv()):", student_data)  # Debugging statement
            for student in student_data.values():
                # Create a new dictionary that maps internal keys to readable keys
                row_to_write = {READABLE_HEADERS[key]: student[key] for key in student}
                writer.writerow(row_to_write)  # Write each student's data
                print(f"Wrote row: {row_to_write}")  # Debug: Show each row being written

        print(f"Data saved to {csv_file} successfully.")  # Confirmation message
    except Exception as e:
        print(f"Error while saving to CSV: {e}")
