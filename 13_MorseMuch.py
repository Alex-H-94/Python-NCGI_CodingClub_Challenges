charToDots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

def ConvertToMorse(originalSentence):
    # Split the 'string' by spaces and put them into a list.
    listOriginalSentence = originalSentence.split()
    listCompleteMorse = []

    for word in listOriginalSentence:
        # For each entry in the list (ie. each word) separate out each letter.
        listOriginalChar = list(word)
        
        # Loop through each letter and select the matching morse code.
        # Capitalize the letter so that 'a' becomes 'A' as the 'in' function matches the characters exactly.
        listMorseChar = []
        for char in listOriginalChar:
            if char.capitalize() in charToDots:
                listMorseChar.append(charToDots[char.capitalize()])
            else:
                print(f"CAUTION: No morse code for '{char}' was found. The final output will not include it.")

        # Add the final result (as a completed string) to the list of new morse coded words.
        # As required, a single space before .join is used to separate characters.
        listCompleteMorse.append(' '.join([str(lr) for lr in listMorseChar]))

    # Finally, do the same thing, but now with every word in the list.
    # As required, three spaces before .join is used to separate words.
    finalResult  = '   '.join([str(wd) for wd in listCompleteMorse])
    return finalResult

userSentence = input("Input your sentence to convert: ")
morseComplete = ConvertToMorse(userSentence)

print(f"Your morse coded sentence: \n{morseComplete}")