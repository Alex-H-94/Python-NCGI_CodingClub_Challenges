lstTestOne = [1]
lstTestZero = [-1, 0, -0, 2, -2]
lstTestZeroAndOne = [0]
lstTestString = [1, -1, 2, "Hello"]
lstTestSequenceFalse = [1,-1,1,2,3,-3,4]
lstTestSequenceTrue = [1,-1,2,-2,3,-3,4]

def IsAlternating(lstSeqToCheck: list):
    # Check the list. If it doesn't pass the checks, don't bother.
    bolLenCheck = len(lstSeqToCheck) <= 1
    bolZeroCheck = 0 in lstSeqToCheck

    if bolLenCheck or bolZeroCheck:
        print("CAUTION: Unable to determine if this is a sequence. " 
              + ("There were less than two elements in the list. " if bolLenCheck else "")
              + ("The list contained a 0 which cannot be alternated. " if bolZeroCheck else ""))
        return False
    
    try:
        bolLastItem = lstSeqToCheck[0] < 0 # Check if the first element is pos or neg.
        for ele in lstSeqToCheck[1:]:
            bolNewItem = ele < 0 # Check if the next element is pos or neg.

            if bolNewItem == bolLastItem: # If it matches the last element, it is not alternating.
                return False
            else:
                bolLastItem = bolNewItem # Get ready to check the next element.
        
        return True # If we get to the end of the list successfully, it must be alternating.
    
    except TypeError:
        print("CAUTION: Unable to determine if this is a sequence. This list contains something that isn't a number.")
        return False
    except Exception as err:
        print(f"CAUTION: There was an unknown error: {err}")
        return False


# Testing the function:

print (f"lstTestOne Result is: {IsAlternating(lstTestOne)}")
print (f"lstTestZero Result is: {IsAlternating(lstTestZero)}")
print (f"lstTestZeroAndOne Result is: {IsAlternating(lstTestZeroAndOne)}")
print (f"lstTestString Result is: {IsAlternating(lstTestString)}")
print (f"lstTestSequenceFalse Result is: {IsAlternating(lstTestSequenceFalse)}")
print (f"lstTestSequenceTrue Result is: {IsAlternating(lstTestSequenceTrue)}")