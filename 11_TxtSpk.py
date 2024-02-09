# def RemoveVowels(textToAlter):
#     newText = ""

#     for letter in textToAlter:
#         if letter not in 'aeiou':
#             newText += letter
    
#     return newText
        

# newSentence = RemoveVowels(userInput)

# print(f"Your converted sentence: \n{newSentence}")

def CheckPhrases(textToCheck):
    distTxtSpk = {}
    modifiedText = textToCheck
    
    # Open the text file and split out phrases into a useable dictionary format.
    # ie. The line 'lol - laugh out load' becomes: '{"laugh out loud": "lol"}.
    # This is done because I wanted to just copy/paste from the wiki and not make a json.
    with open('txtspk_phrases.txt') as file:
        fileLines = file.readlines()
                
        for line in fileLines:
            splitText = str(line).strip().split(' - ')
            distTxtSpk[splitText[1]] = splitText[0]
    
    # Now check if there are any matching phrases in the text.
    for phrase in distTxtSpk:
                
        # if phrase in textToCheck.lower():
        #     # Record the position in the string.
        #     pos = textToCheck.find(phrase)
        #     # Insert the txtSpk version of the phrase in its place.
        #     modifiedText = modifiedText[:pos] + distTxtSpk[phrase] + textToCheck[pos+len(phrase):]
        
        for x in textToCheck.lower() if x in phrase:
            print(f"Checking {phrase} and found something!")
        else:
            print(f"Checking {phrase} and found nothing...")


userInput = input("Input your sentence to translate into TxtSpk: \n")
CheckPhrases(userInput)