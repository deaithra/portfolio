'''
Daisy Williams
Project 2
Random Number
'''

def main():

    #import module
    #random - generate random number
    import random     

    #Introduction
    print("Welcome to our number guessing game!\n")
    print("The object of the game is to guess the secret number. " +
          "You will enter your numerical guess from any number between 1 and 100. " +
          "You will have clues after your guess to let you know if the number is higher or lower than your guess. " +
          "Once you have guessed the secret number, you win the game! You have 10 tries.\n")

    #Menu Options
    def startGame():
        menuSelection = input("To begin the game enter 1. To quit, enter 2: ")
        if (str(menuSelection) == "1"):
            #test
            print ("\nYou entered: " + str(menuSelection) + ". Let's begin!")

            #pick a random number
            randomNumber = random.randint(1, 101)
            #test
            #print (str(randomNumber))

            #prompt user to guess the number
            numGuesses = 0
            guessesLeft  = 10
            while numGuesses < 10:
                guess = input("\nGuess the secret number. Choose any number between 1 - 100: ")
                numGuesses += 1
                
                if (str(guess) == str(randomNumber)):
                    print("\nGreat job! After " + str(numGuesses) + " chances, the number you guessed (" + str(guess) + ") matches the secret number.")
                    playAgain = input("\nTo play again press 1. To exit, press 2: \n")
                    if (str(playAgain) == "1"):
                        startGame()
                    elif (str(playAgain) == "2"):
                        print("Goodbye!")
                    else:
                        print ("\nInvalid entry. Please enter 1 or 2: ")

                #if guess does not match, indicate higher or lower
                else:
                    guessesLeft -= 1
                    print("\nSorry, the number you entered does not match the secret number.")
                    print ("\nYou have " + str(guessesLeft) + " guesses left")
                    if (str(guess) < str(randomNumber)):
                        print("\n" + str(guess) + " is lower than the random number. Try guessing a higher number. ")
                    else:
                        print("\n" + str(guess) + " is higher than the random number. Try guessing a lower number. ")         
               
        elif (str(menuSelection) == "2"):
            print("Goodbye!")

        else:
            print ("\nInvalid entry. Please enter 1 or 2: ")
    startGame()

main()
