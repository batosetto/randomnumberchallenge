import random

def getRandomNumber():
    min_val = int(input("Type minimum number: "))
    max_val = int(input("Type maximum number: "))
    return random.randint(min_val, max_val)

def isDivisibleBy3And5(num):
    return num % 3 == 0 and num % 5 == 0

def printStatisticsAndReset(winnings, total_games):
    print(f"You have won {winnings} out of {total_games} games.")
    print(f"Your winning percentage is: {winnings/total_games*100:0.2f}%")
    reset = input("Would you like to reset the win/loss statistics? (y/n): ").lower()
    if reset == "y":
        print("Game has been reset")
        return 0, 0  
    else:
        print("Game has not been reset")
        return winnings, total_games  

number_to_guess = getRandomNumber()
guess = int(input("Guess the number: "))

winnings = 0
total_games = 0

while True:
    total_games += 1
    if guess == number_to_guess:
        print("You guessed the number!")
        winnings += 1
        if isDivisibleBy3And5(number_to_guess):
               print("The number was divisible by 3 and 5")
        else:
                print("The number was not divisible by 3 and 5")
        break
    else: 
        print("Try again!")
        continue_guessing = input("Do you want to continue guessing? (y/n): ").lower()
        if continue_guessing == "n":
            print(f"The number was: {number_to_guess}")
            if isDivisibleBy3And5(number_to_guess):
               print("The number was divisible by 3 and 5")
            else:
                print("The number was not divisible by 3 and 5")
            break 

        guess = int(input("Guess the number: "))

winnings, total_games = printStatisticsAndReset(winnings, total_games)
