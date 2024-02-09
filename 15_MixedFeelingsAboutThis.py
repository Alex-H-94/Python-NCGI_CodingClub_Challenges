from random import shuffle

def ScrambleSentence(sentenceToScramble):
    # Split the 'string' by spaces and put them into a list.
    listSentence = sentenceToScramble.split()
    listScrambledSentence = []

    for word in listSentence:
        # For each entry in the list (ie each word) separate out each letter.
        scrambledWord = list(word)

        # Record the first and last letter, then remove them.
        firstLetter = scrambledWord[0]
        lastLetter = scrambledWord[-1]
        scrambledWord.pop(0)
        scrambledWord.pop(-1)

        # Scramble the remaining letters.
        shuffle(scrambledWord)

        # Put the first and last letters back in.
        scrambledWord.insert(0, firstLetter)
        scrambledWord.append(lastLetter)

        # Add the final result (as a completed string) to the list of new scrambled words.
        listScrambledSentence.append(''.join([str(lr) for lr in scrambledWord]))

    # Finally, do the same thing, but now with every word in the list.
    finalResult  = ' '.join([str(wd) for wd in listScrambledSentence])
    return finalResult

userSentence = input("Input your sentence to scramble: ")
scrambledComplete = ScrambleSentence(userSentence)

print(f"Your scrambled sentence: \n{scrambledComplete}")