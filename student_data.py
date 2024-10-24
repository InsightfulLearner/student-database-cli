import csv
import os
from constants import INTERNAL_HEADERS, READABLE_HEADERS

student_data = {}

def load_from_csv():
    global student_data

    csv_file = "student_database.csv"
    
    if not os.path.exists(csv_file):
        print(f"{csv_file} not found. Creating a new file with headers.")
        with open(csv_file, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=READABLE_HEADERS.values())
            writer.writeheader()
        student_data = {}
        return

    try:
        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            student_data = {}
            print(f"Reading from {csv_file}...")
            for row in reader:
                uid = row.get("Student ID", "").strip()
                if uid:
                    print(f"Extracted UID: '{uid}'")
                    student_data[uid] = {
                        INTERNAL_HEADERS[header.strip()]: row[header].strip()
                        for header in reader.fieldnames
                        if header.strip() in READABLE_HEADERS.values()
                    }
            print(f"Loaded student data: {student_data}")
    except Exception as e:
        print(f"Error while loading data: {e}")

# Load data when this module is imported
load_from_csv()
