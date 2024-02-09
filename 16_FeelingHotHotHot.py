def ConvertToFahrenheit(userTemp):
    newTemp = round((int(userTemp) * 1.8) + 32, 2)
    return newTemp

def getNumericInput(inpQuestion):
    userVal = input(inpQuestion)
    while not userVal.isnumeric():
        print("Enter only a number.")
        userVal = input("Try again: ")
    return int(userVal)

#tempInCel = input("Input your temperature in Celsius: ")

tempInCel = getNumericInput("Input your temperature in Celsius: ")
tempInFah = ConvertToFahrenheit(tempInCel)

print(f"{tempInCel} *C = {tempInFah} *F")