from student_management import student_management
from student_data import student_data


# ==========================
# Main Function
# ==========================
def main():

    print("After loading, student data is:", student_data)  # Debugging line
    while True:
        student_management() # Initial menu and user input handling


if __name__ == "__main__":
    main()