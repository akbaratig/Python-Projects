import random


def validate_input(user_guess):
    if not user_guess.isdigit():
        print("Invalid Input. Please Try Again !!")
        return False
    
    user_guess = int(user_guess)
    if (user_guess < 0) or (user_guess > 100):
        print("Your Guess is Out of Range. Please Try again. Your Guess should be between 1 and 100.")
        return False
    
    return user_guess


def main():
    random_number = random.randint(1, 100)
    
    score = 100
    while True:
        print('*' * 50)
        user_guess = input("Guess a Number Betwwen 1 And 100 : ")
    
        if user_guess == 'q':
            print("Thank You for playing. GoodBye!")
            break
    
        if not validate_input(user_guess):
            continue
    
        print(f"Your Guess is : {user_guess}") 
        user_guess = int(user_guess)
    
        if user_guess > random_number:
            print("Your Guess is too high. Please Try again")
        elif user_guess < random_number:
            print("Your Guess is too low. Please Try again")
        else :
            print("Congratulations !!!! You Guessed the Correct Number.")
            print(f"Your Score is : {score}")
            temp = input("Do you want to play again ? (y/n) : ")
            if temp.lower() == 'y':
                main()
            break
    
    score -= 5 
    score = max(score, 0)
    
    



if __name__ == '__main__':
    print("Welcome to the Number Guessing Game !!")
    main()
