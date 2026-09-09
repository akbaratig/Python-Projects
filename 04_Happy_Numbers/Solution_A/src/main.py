def check_happy_number(n):
    """"Check if a number is a happy number."""
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    
    if n == 1:
        return True
    else:
        return False
    


if __name__ == "__main__":
    while True:
        try:
            print("Welcome to the Happy Number Checker!")
            print("=" * 50)
            number = input("Enter a positive integer to check if it's a happy number (or type 'exit' to quit): ")
            if number == 'q' or number == 'exit':
                print("Exiting the Happy Number Checker. Goodbye!")
                break
            if int(number) <= 0:
                print("Please enter a positive integer.")
                continue
            if check_happy_number(int(number)):
                print(f"{number} is a happy number.")
            else:
                print(f"{number} is not a happy number.")
        except ValueError:
            print("Invalid input. Please enter a positive integer or type 'q' to quit.")