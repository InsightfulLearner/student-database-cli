import sys


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