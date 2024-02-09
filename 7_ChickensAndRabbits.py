def findChickenAndRabbits(heads, legs):
    # Find the maximum amount of legs you could possibly have.
    maximumLegs = heads * 4
    
    # Do some checks before doing any calculations.
    if legs > maximumLegs:
        print("Unless there are chicken/rabbit centaurs: No solution.")
        return
    
    if heads >= (legs/2) or (legs % 2):
        print("Unless there are chicken/rabbit amputees: No solution.")
        return
    
    # Get the difference between the maximum and current amount of legs, then divide that by 2 (legs per chicken).
    chickens = (maximumLegs - legs) / 2
    # See the remainder for rabbits.
    rabbits = heads - chickens
    
    print(f"There are {chickens} chickens, and {rabbits} rabbits.")
    return

def GetNumericInput(inpQuestion):
    userVal = input(inpQuestion)
    while not userVal.isnumeric():
        print("Enter only a number.")
        userVal = input("Try again: ")
    return int(userVal)

userNumOfHeads = GetNumericInput("How many heads are there? ")
userNumOfLegs = GetNumericInput("How many legs are there? ")

findChickenAndRabbits(userNumOfHeads, userNumOfLegs)