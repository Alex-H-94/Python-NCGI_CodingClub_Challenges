from random import randint
from math import floor

numOfDragons = randint(2,10)
numOfArrowsToKill = randint(2,10)

def GetNumericInput(inpQuestion):
    userVal = input(inpQuestion)
    while not userVal.isnumeric():
        print("Enter only a number.")
        userVal = input("Try again: ")
    return int(userVal)

def DoesUserSucceed(takenArrows, dragons):
    if (numOfArrowsToKill * dragons) <= takenArrows:
        return True
    else:
        return False

print(f"You have encountered {numOfDragons} dragon(s)! \nIt takes {numOfArrowsToKill} arrows per dragon to kill them...")

userArrows = input("How many arrows do you take on your adventure? ")

if DoesUserSucceed(userArrows, numOfDragons):
    print("You win!")
else:
    deadDragons = floor(userArrows / numOfArrowsToKill)
    print(f"You manage to slay {deadDragons} dragons, but as you reach for your next arrow you find the quiver empty. You did not bring enough! and have become a dragon's snack.")