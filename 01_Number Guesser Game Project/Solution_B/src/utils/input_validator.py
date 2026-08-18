def get_valid_input(start, end):
    """Get a valid integer input from the user between start and end (inclusive)."""
    while True:
        try:
            user_input = int(input("Please Enter a Number : "))
            if start <= user_input <= end:
                return user_input
            else:
                print(f"Please enter a number between {start} and {end}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
