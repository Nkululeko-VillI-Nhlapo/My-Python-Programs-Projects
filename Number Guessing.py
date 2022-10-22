# Name: Nhlapo Nkululeko
# StuN: 4129962
# GUESSSING GAME

import random

randGen = random.Random()
numb = randGen.randrange(1, 10)

playerGuess = 0
response = ""

while playerGuess != numb:
    playerGuess = int(input(response + "\nGuess my number between 1 and 10. Enter 0 to Quit: "))

    if playerGuess > numb:
        response += str(playerGuess) + " It's too high.\n"

    elif playerGuess < numb:
        response += str(playerGuess) + " It's too low.\n"

print(f"{playerGuess} is Correct!!!")