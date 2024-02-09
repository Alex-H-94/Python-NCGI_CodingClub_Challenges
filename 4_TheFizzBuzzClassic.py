def CheckFizzBuzz(numToCheck):
    strReturn = ""
    if int(numToCheck) % 3 == 0: strReturn += "Fizz"
    if int(numToCheck) % 5 == 0: strReturn += "Buzz"

    if not strReturn: # String is empty.
        return numToCheck
    else:
        return strReturn

usrInput = input("Comparing if numbers are divisible by 3 (Fizz) and 5 (Buzz). Enter a number to be checked: \n")
print(CheckFizzBuzz(usrInput))