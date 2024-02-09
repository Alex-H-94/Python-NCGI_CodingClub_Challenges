# Simple Version

# def CountChar(inpToCheck = ""):
#     return inpToCheck.lower().count('x') == inpToCheck.lower().count('o'):

# userInp = input(f"Comparing if number of X and O's are the same. Enter a string to be checked: \n")
# print (f"The result is: {CountChar(userInp)}")


# Complicated Version

def CountCharAndCompare(inpToCheck: str):
    numOfX = inpToCheck.lower().count('x')
    numOfO = inpToCheck.lower().count('o')

    return [(numOfX == numOfO), numOfO, numOfX]

userInp = input(f"Comparing if number of X and O's are the same. Enter a string to be checked: \n")
lstResults = CountCharAndCompare(userInp)

print(f"The result is: {lstResults[0]}. There are [{lstResults[1]}] X's and [{lstResults[2]}] O's in your string, which is " + ("the same." if lstResults[0] else "different."))