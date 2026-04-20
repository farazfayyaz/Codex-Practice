# Rock, Paper, Scissors Game

# Rules:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
import random # import random module

#create intro screen
print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊ - Rock")
print("2) ✋ - Paper")
print("3) ✌️ - Scissors")

player = int(input("Pick a number: ")) # get user input
computer = random.randint(1, 3) # generate CPU input

print("\n") # spacer

# conditionals
if (player == 1 and computer == 2):
    print("You Chose: ✊ - Rock")
    print("CPU Chose: ✋ - Paper\n")
    print("The Computer Won!")
elif (player == 1 and computer == 3):
    print("You Chose: ✊ - Rock")
    print("CPU Chose: ✌️ - Scissors\n")
    print("The Player Won!")
elif (player == 1 and computer == 1):
    print("You Chose: ✊ - Rock")
    print("CPU Chose: ✊ - Rock\n")
    print("Tie!")
elif (player == 2 and computer == 2):
    print("You Chose: ✋ - Paper")
    print("CPU Chose: ✋ - Paper\n")
    print("Tie")
elif (player == 2 and computer == 3):
    print("You Chose: ✋ - Paper")
    print("CPU Chose: ✌️ - Scissors\n")
    print("The Computer Won!")
elif (player == 2 and computer == 1):
    print("You Chose: ✋ - Paper")
    print("CPU Chose: ✊ - Rock\n")
    print("The Player Won!")
if (player == 3 and computer == 2):
    print("You Chose: ✌️ - Scissors")
    print("CPU Chose: ✋ - Paper\n")
    print("The Player Won!")
elif (player == 3 and computer == 3):
    print("You Chose: ✌️ - Scissors")
    print("CPU Chose: ✌️ - Scissors\n")
    print("Tie!")
elif (player == 3 and computer == 1):
    print("You Chose: ✌️ - Scissors")
    print("CPU Chose: ✊ - Rock\n")
    print("The Computer Won!")