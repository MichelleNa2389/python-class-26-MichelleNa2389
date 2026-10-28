#CS 31 Lab Activity 4
# Michelle Najera
# October 21, 2026

#easy = range of 1 to 10, limit tries to 5.
#medium = range of 1 to 100, limit tries to 8.
#hard = range of 1 to 1000, limit tries to 10.

#tittle display function
def display_tittle():
    print("-" * 80)
    print()
    print("                       Guess The Number Game")
    print()
    print("-" * 80)


def play_game():
    import random
    print("Level Menu")
    print("""        E: Easy = range of 1 to 10, limit 5 attempts.
        M: Medium = range of 1 to 100, liimit 8 attempts.
        H: Hard = range of 1 to 1000, limit 10 attempts.
    """)

    your_level= input("Which level would you like to play? E/M/H: ")
    if your_level.lower() == "e":
        LIMIT = 10
        attempts = 5
    elif your_level.lower() == "m":
        LIMIT = 100
        attempts = 8
    elif your_level.lower() == "h":
        LIMIT = 1000
        attempts = 10
    else:
        LIMIT =10000
        attempts = 5

    secret_number = random.randint(1, LIMIT) 
    print()
    print (f"I'm thinking of a number from 1 to {LIMIT}\n")
    count = 1 # keeps track of the number of attemps
    

    while (guess := int(input ("Your guess:"))) != secret_number: # != means does not equal := means equal (waluars)
        if count >= attempts:
            print("Sorry! You ran out of attempts =(")
            print()
            break
        if guess< secret_number:
            print("Sorry your guess is too low")
            print()
        elif guess > secret_number:
            print("Sorry your guess is too high")
            print()
        count += 1
    else: 
         print()
         print(f"Congratulations! You guessed the number in {count} attempts\n")
      
        
     
def main():
    display_tittle()
    player_name = input("Hi there! What's your name? ")
    print()

    again= "y"
    while again.lower() == "y":
        play_game()
        again = input (f"Would you want to play another round of the game {player_name}? (y/n):\n")
        print()

    print("Thanks for playing! Goodbye!")
    print()


if __name__ == "__main__":
    main()
