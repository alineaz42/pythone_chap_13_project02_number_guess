# ******************go to score board and set it to 100 first******************
# number guessing game
# project two
# from Code With Harry
# Ali Neaz:
import random
randNumber = random.randint(1, 100)
guesses = 0
userGuess = None

# print(randNumber)
while userGuess != randNumber:
    userGuess = int(input("Enter  your guess: \n"))
    guesses += 1
    if randNumber == userGuess:
        print(f"computer guessed: {randNumber} and you guessed: {userGuess} ")
        print("You guessed it right")
    else:
        if userGuess > randNumber:
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")


print(f"You guessed the number in {guesses} ")


with open("highscore.txt", "r") as f:
    highscore = int(f.read())


if guesses < highscore:
    print(f"You have just broke the hiscore ur guesses are: {guesses} ")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))  # don't forget to convert in str


# **************************need to work in this one later**************************
# # first opening the score board
# with open("highscore.txt", "r") as f:
#     firstReading = int(f.read())
# if firstReading == None:
#     with open("highscore.txt", "w") as f:
#         f.write(str(guesses))
# else:
#     with open("highscore.txt", "a") as f:
#         hiscore = int(f.read())
#     if guesses < hiscore:
#         print(f"You just broke the hiscore \n your score is {guesses} ")
#         with open("highscore.txt", "w") as f:
#             f.write(str(guesses))
