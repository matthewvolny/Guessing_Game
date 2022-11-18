import random

from art import logo

print(logo)

def guessing_game():

    continue_game = 'y'

    while continue_game == 'y':

        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        
        random_num = random.randint(0, 100)
        # print(random_num)

        attempts = 0

        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        
        if difficulty == 'easy':
            attempts = 10
        elif difficulty == 'hard':
            attempts = 5
        
        while attempts > 0:

            print(f"You have {attempts} attempts to guess the number.")
        
            guess = int(input("Make a Guess: "))
            
            while guess != random_num:
                if guess > random_num:
                    print("Too high.")
                    print("Guess again.")
                elif guess < random_num:
                    print("Too low.")
                    print("Guess again.")
                attempts -= 1
                if attempts == 0:
                    print("You've run out of guesses, you lose.")
                    break
                else:
                    print(f"You have {attempts} attempts to guess the number.")
                    guess = int(input("Make a Guess: "))
            
            if attempts != 0:
                print("You guessed the number. You win!")
            
            continue_game = input("Would you like to play again? Type y or n.")
            
            if continue_game == 'y':
                guessing_game()   

        continue_game = input("Would you like to play again? Type y or n.")
        
        if continue_game == 'y':
                guessing_game()

guessing_game()